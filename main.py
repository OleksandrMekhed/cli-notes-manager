import argparse
import sys
from notes.storage import JsonStorage
from notes.models import NoteManager


def main():
    parser = argparse.ArgumentParser(description="Console note manager (CLI)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show details debug")

    subparsers = parser.add_subparsers(dest="command", required=True)


    add_parser = subparsers.add_parser("add", help="Add new note")
    add_parser.add_argument("-t", "--title", required=True, help="Title note")
    add_parser.add_argument("-c", "--content", required=True, help="Text note")


    subparsers.add_parser("list", help="Show all notes")


    del_parser = subparsers.add_parser("delete", help="Delete note with given ID")
    del_parser.add_argument("id", type=int, help="ID notes for delete")

    args = parser.parse_args()

    storage = JsonStorage()
    manager = NoteManager(storage=storage, verbose=args.verbose)

    if args.command == "add":
        manager.add_note(args.title, args.content)
        print(f"Notes '{args.title}' added!")

    elif args.command == "list":
        notes = manager.list_notes()
        if not notes:
            print("List of notes is empty.")
            return
        print("-" * 40)
        for n in notes:
            print(f"ID: {n.id} | [{n.created_at}]")
            print(f"Title: {n.title}")
            print(f"text: {n.content}")
            print("-" * 40)

    elif args.command == "delete":
        success = manager.delete_note(args.id)
        if success:
            print(f"Note with ID={args.id} deleted.")
        else:
            print(f"Note with ID={args.id} not found.")
            sys.exit(1)


if __name__ == "__main__":
    main()