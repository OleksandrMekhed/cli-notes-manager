from datetime import datetime


class Note:
    def __init__(self, title: str, content: str, note_id = None):
        self.id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        note = cls(
            title = data["title"],
            content = data["content"],
            note_id = data["id"]
        )
        note.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M"))
        return note



class NoteManager:
    def __init__(self, storage, verbose: bool = False):
        self.storage = storage
        self.verbose = verbose
        self.notes = self.storage.load()


    def _log(self, message: str):
        if self.verbose:
            print(f"[VERBOSE] {datetime.now().strftime('%H:%M:%S')} -> {message}")



    def add_note(self, title: str, content: str) -> None:
        self._log(f"Adding note with title: {title}")
        new_id = max([n.id for n in self.notes], default=0) + 1
        note = Note(title=title, content=content, note_id=new_id)
        self.notes.append(note)
        self.storage.save(self.notes)
        self._log(f"Added note with id: {new_id}")
        return note

    def list_notes(self) -> list[Note]:
        self._log(f"Listing all notes. Total notes: {len(self.notes)}")
        return self.notes

    def delete_note(self, note_id: int) -> bool:
        self._log(f"Deleting note with id: {note_id}")
        initial_count = len(self.notes)
        self.notes = [n for n in self.notes if n.id != note_id]

        if len(self.notes) < initial_count:
            self.storage.save(self.notes)
            self._log(f"Deleted note with id: {note_id}")
            return True

        self._log(f"No note with id: {note_id}")
        return False
