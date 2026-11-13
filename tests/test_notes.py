import unittest
from notes.models import NoteManager


class MockStorage:


    def __init__(self):
        self.data = []

    def load(self):
        return self.data

    def save(self, notes):
        self.data = notes


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.storage = MockStorage()
        self.manager = NoteManager(storage=self.storage, verbose=False)

    def test_add_note(self):
        note = self.manager.add_note("Test Title", "Test Content")
        self.assertEqual(note.id, 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(len(self.manager.list_notes()), 1)

    def test_delete_note(self):
        self.manager.add_note("To Delete", "Content")
        self.assertEqual(len(self.manager.list_notes()), 1)

        success = self.manager.delete_note(1)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.list_notes()), 0)

    def test_delete_non_existent(self):
        success = self.manager.delete_note(999)
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()