import random
import unittest

from engine import LETTERS, PRIZES, check_answer, create_game, current_prize, difficulty_for_level, guaranteed_prize, select_question, use_audience, use_fifty, use_friend, visible_choices
from questions import QUESTIONS, QUESTIONS_BY_ID


class EngineTests(unittest.TestCase):
    def test_all_questions_have_four_options_and_one_correct_index(self):
        self.assertEqual(len(QUESTIONS), len(QUESTIONS_BY_ID))
        for question in QUESTIONS:
            self.assertEqual(len(question["options"]), 4)
            self.assertIn(question["correct"], range(4))
            self.assertIn(question["difficulty"], ("easy", "medium", "hard"))

    def test_each_round_has_enough_questions(self):
        for name in ("easy", "medium", "hard"):
            self.assertGreaterEqual(sum(q["difficulty"] == name for q in QUESTIONS), 5)

    def test_initial_state(self):
        state = create_game()
        self.assertEqual(state["level"], 0)
        self.assertIsNone(state["question_id"])
        self.assertEqual(state["asked_ids"], [])
        self.assertFalse(any(state["used_hints"].values()))

    def test_question_stays_same_until_answered(self):
        state = create_game()
        question = select_question(state, random.Random(1))
        self.assertEqual(select_question(state, random.Random(2)), question)
        self.assertEqual(len(state["asked_ids"]), 1)

    def test_questions_do_not_repeat(self):
        state = create_game()
        rng = random.Random(123)
        for index in range(15):
            question = select_question(state, rng)
            self.assertEqual(question["difficulty"], difficulty_for_level(index))
            self.assertTrue(check_answer(state, LETTERS[question["correct"]]))
        self.assertEqual(state["level"], 15)
        self.assertEqual(len(set(state["asked_ids"])), 15)
        self.assertIsNone(select_question(state))

    def test_incorrect_answer_keeps_level(self):
        state = create_game()
        question = select_question(state, random.Random(2))
        wrong = next(i for i in range(4) if i != question["correct"])
        self.assertFalse(check_answer(state, LETTERS[wrong]))
        self.assertEqual(state["level"], 0)

    def test_letters_are_case_insensitive(self):
        state = create_game()
        question = select_question(state)
        self.assertTrue(check_answer(state, LETTERS[question["correct"]].lower()))

    def test_invalid_answers_raise(self):
        state = create_game()
        select_question(state)
        with self.assertRaises(ValueError):
            check_answer(state, "z")
        with self.assertRaises(ValueError):
            check_answer(state, "")

    def test_fifty_removes_exactly_two_incorrect(self):
        state = create_game()
        question = select_question(state)
        remaining = use_fifty(state, random.Random(1))
        self.assertEqual(len(remaining), 2)
        self.assertIn(question["correct"], remaining)
        self.assertEqual(len(state["hidden_choices"]), 2)
        with self.assertRaises(ValueError):
            use_fifty(state)
        with self.assertRaises(ValueError):
            check_answer(state, LETTERS[state["hidden_choices"][0]])

    def test_friend_selects_visible_option(self):
        state = create_game()
        select_question(state)
        use_fifty(state)
        answer = use_friend(state, random.Random(2))
        self.assertIn(LETTERS.index(answer), visible_choices(state))
        with self.assertRaises(ValueError):
            use_friend(state)

    def test_audience_percentages_total_100(self):
        for fifty in (False, True):
            state = create_game()
            select_question(state)
            if fifty:
                use_fifty(state)
            results = use_audience(state, random.Random(3))
            self.assertEqual(sum(results.values()), 100)
            self.assertEqual(set(results), set("ABCD"))
            for hidden in state["hidden_choices"]:
                self.assertEqual(results[LETTERS[hidden]], 0)
            with self.assertRaises(ValueError):
                use_audience(state)

    def test_hints_are_not_reset_after_correct_answer(self):
        state = create_game()
        question = select_question(state)
        use_friend(state)
        check_answer(state, LETTERS[question["correct"]])
        select_question(state)
        with self.assertRaises(ValueError):
            use_friend(state)

    def test_prizes_and_safe_levels(self):
        self.assertEqual(len(PRIZES), 15)
        self.assertEqual(PRIZES[-1], 1000000)
        self.assertEqual(current_prize(0), 0)
        self.assertEqual(current_prize(5), 5000)
        self.assertEqual(guaranteed_prize(4), 0)
        self.assertEqual(guaranteed_prize(5), 5000)
        self.assertEqual(guaranteed_prize(9), 5000)
        self.assertEqual(guaranteed_prize(10), 125000)
        self.assertEqual(guaranteed_prize(14), 125000)
