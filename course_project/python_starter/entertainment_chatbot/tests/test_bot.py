
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from bot.data import RECOMMENDATIONS
from bot.entertainment import get_genres, recommend_item, ukrainian_joke, interesting_story
from bot.games import number_hint, rock_paper_scissors_result
from main import main


class EntertainmentTests(TestCase):
    def test_all_categories_have_genres(self):
        for category in ("movies", "music", "video_games"):
            self.assertGreater(len(get_genres(category)), 0)

    def test_recommendation_belongs_to_selected_genre(self):
        for category, genres in RECOMMENDATIONS.items():
            for genre, items in genres.items():
                with self.subTest(category=category, genre=genre):
                    self.assertIn(recommend_item(category, genre), items)

    def test_unknown_genre(self):
        with self.assertRaises(ValueError):
            recommend_item("movies", "Несуществующий жанр")

    def test_joke_and_story_are_nonempty(self):
        self.assertTrue(ukrainian_joke())
        self.assertTrue(interesting_story())


class GamesTests(TestCase):
    def test_rock_beats_scissors(self):
        self.assertEqual(rock_paper_scissors_result("Камінь", "Ножиці"), "win")

    def test_scissors_lose_to_rock(self):
        self.assertEqual(rock_paper_scissors_result("Ножиці", "Камінь"), "lose")

    def test_all_ties(self):
        for move in ("Камінь", "Ножиці", "Папір"):
            self.assertEqual(rock_paper_scissors_result(move, move), "draw")

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            rock_paper_scissors_result("Динаміт", "Камінь")

    def test_number_hints(self):
        self.assertEqual(number_hint(7, 12), "higher")
        self.assertEqual(number_hint(19, 12), "lower")
        self.assertEqual(number_hint(12, 12), "correct")


class IntegrationTests(TestCase):
    def test_can_exit_from_main_menu(self):
        output = StringIO()
        with patch("builtins.input", return_value="0"), redirect_stdout(output):
            main()
        self.assertIn("До зустрічі", output.getvalue())

    def test_can_navigate_games_menu(self):
        output = StringIO()
        with patch("builtins.input", side_effect=["7", "0", "0"]), redirect_stdout(output):
            main()
        self.assertIn("Мініігри", output.getvalue())
        self.assertIn("До зустрічі", output.getvalue())


class InteractiveGameTests(TestCase):
    def test_guess_number_win(self):
        from bot.games import play_guess_number
        output = StringIO()
        with patch("bot.games.random.randint", return_value=12), \
             patch("builtins.input", side_effect=["7", "12"]), redirect_stdout(output):
            play_guess_number()
        self.assertIn("Загадане число більше", output.getvalue())
        self.assertIn("Вітаю!", output.getvalue())

    def test_rock_paper_scissors_win_and_return(self):
        from bot.games import play_rock_paper_scissors
        output = StringIO()
        with patch("bot.games.random.choice", return_value="Ножиці"), \
             patch("builtins.input", side_effect=["1", "0"]), redirect_stdout(output):
            play_rock_paper_scissors()
        self.assertIn("Ви перемогли!", output.getvalue())

    def test_guess_number_ignores_invalid_input(self):
        from bot.games import play_guess_number
        output = StringIO()
        with patch("bot.games.random.randint", return_value=15), \
             patch("builtins.input", side_effect=["abc", "21", "0"]), redirect_stdout(output):
            play_guess_number()
        self.assertEqual(output.getvalue().count("Введіть ціле число"), 2)
