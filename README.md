# CliNotesManager

A simple console note manager written in Python. Notes are stored in a local JSON file, and everything is controlled through CLI commands.

## Features

- Add notes with a title and content
- List all notes with ID and creation date
- Delete a note by ID
- Optional verbose mode for debug output
- Unit tests with a mock storage (no real files touched)

## Requirements

- Python 3.14+ (the code uses the `str | Path` type syntax)
- No third-party dependencies

## Project structure

```
CliNotesManager/
├── main.py              # CLI entry point (argparse)
├── notes/
│   ├── models.py        # Note and NoteManager classes
│   └── storage.py       # JsonStorage: reads/writes notes.json
├── tests/
│   └── test_notes.py    # unit tests for NoteManager
└── notes.json           # created automatically on first save
```

## Usage

Run all commands from the project root:

```bash
# Add a note
python main.py add -t "Shopping" -c "Buy milk and bread"

# Show all notes
python main.py list

# Delete a note by ID
python main.py delete 1

# Any command with detailed logs (-v goes BEFORE the command)
python main.py -v list
```

If your system uses `python3` instead of `python`, use that.

### Commands

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add` | `-t/--title`, `-c/--content` (both required) | Add a new note |
| `list` | none | Show all notes |
| `delete` | `id` (integer) | Delete the note with the given ID |

| Global option | Description |
|---------------|-------------|
| `-v`, `--verbose` | Print debug messages with timestamps |

## Storage

Notes are saved in `notes.json`. The path is relative, so the file is created in the directory you run the program from (the project root when launched from PyCharm).

Each note looks like this:

```json
{
    "id": 1,
    "title": "Shopping",
    "content": "Buy milk and bread",
    "created_at": "2026-11-13 14:30"
}
```

IDs are assigned as `max(existing IDs) + 1`.

## Running tests

```bash
python -m unittest tests.test_notes
```

In PyCharm: right-click `tests/test_notes.py` → Run.

## Architecture

- **`Note`**: a plain data class with `to_dict()` / `from_dict()` for JSON conversion.
- **`NoteManager`**: business logic (add, list, delete). It receives a storage object, so it does not care where the data lives.
- **`JsonStorage`**: implements `load()` and `save()` for a JSON file. Any object with these two methods can replace it (the tests use an in-memory `MockStorage`).

## Ideas for further development

- `search` command (find notes by text)
- Tags for notes
- `export` to Markdown
- Reading note text from stdin