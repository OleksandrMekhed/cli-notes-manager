import json
import os
from .models import Note



class JsonStorage:
    def __init__(self, filepath: str =  ".notes.json"):
        self.filepath = filepath

    def load(self) -> list[Note]:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Note.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []

    def save(self, notes: list[Note]):
        data = [note.to_dict() for note in notes]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)