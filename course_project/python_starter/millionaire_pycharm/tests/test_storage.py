import tempfile
import unittest
from pathlib import Path

from engine import create_game, select_question, use_fifty
from storage import delete_save, load_game, load_stats, record_result, save_game


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.save_path = Path(self.temporary.name) / "save.json"
        self.stats_path = Path(self.temporary.name) / "stats.json"

    def test_save_and_load_preserve_question_and_hints(self):
        state = create_game()
        select_question(state)
        use_fifty(state)
        save_game(state, self.save_path)
        self.assertEqual(load_game(self.save_path), state)

    def test_missing_save_is_not_a_game(self):
        self.assertIsNone(load_game(self.save_path))

    def test_corrupted_save_is_not_loaded(self):
        self.save_path.write_text("{wrong", encoding="utf-8")
        self.assertIsNone(load_game(self.save_path))

    def test_missing_question_is_rejected(self):
        state = create_game()
        state["question_id"] = "invalid-id"
        save_game(state, self.save_path)
        self.assertIsNone(load_game(self.save_path))

    def test_save_can_be_deleted(self):
        save_game(create_game(), self.save_path)
        delete_save(self.save_path)
        self.assertFalse(self.save_path.exists())

    def test_stats_after_two_games(self):
        record_result(5, True, 5000, self.stats_path)
        stats = record_result(15, False, 1000000, self.stats_path)
        self.assertEqual(stats["games"], 2)
        self.assertEqual(stats["victories"], 1)
        self.assertEqual(stats["correct"], 20)
        self.assertEqual(stats["wrong"], 1)
        self.assertEqual(stats["earned"], 1005000)
        self.assertEqual(stats["best"], 1000000)
        self.assertEqual(load_stats(self.stats_path), stats)

    def test_stats_start_empty(self):
        self.assertEqual(load_stats(self.stats_path)["games"], 0)
