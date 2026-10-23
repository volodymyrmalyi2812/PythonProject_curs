import io
import unittest
from unittest.mock import patch

import main


class ConsoleTests(unittest.TestCase):
    def test_menu_exits(self):
        with patch("builtins.input", return_value="0"), patch("sys.stdout", new_callable=io.StringIO) as output:
            main.main()
        self.assertIn("До зустрічі", output.getvalue())

    def test_rules_show_all_hints(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            main.show_rules()
        self.assertIn("50/50", output.getvalue())
        self.assertIn("Дзвінок другу", output.getvalue())
        self.assertIn("Допомога залу", output.getvalue())

    def test_prize_format(self):
        self.assertEqual(main.money(1000000), "1 000 000 грн")
