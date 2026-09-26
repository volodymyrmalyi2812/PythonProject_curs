"""
Модуль unittest предоставляет множество функций для самых различных проверок:

assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc
assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc и сообщение соответствует
регулярному выражению r
assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение
assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение и сообщение соответствует
регулярному выражению r
assertAlmostEqual(a, b) — round(a-b, 7) == 0
assertNotAlmostEqual(a, b) — round(a-b, 7) != 0
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
assertRegex(s, r) — r.search(s)
assertNotRegex(s, r) — not r.search(s)
assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен
"""

import datetime
import sys
import unittest.mock


class UserTestCase(unittest.TestCase):
    # Методы могут быть пропущены:
    @unittest.skip('Test Skip')
    def test_just_skip(self):
        self.fail('Does not run')

    @unittest.skipIf(datetime.datetime.now().hour in [18, 19, 20, 21, 22], 'too late')
    def test_just_skip_if(self):
        self.fail('Does not run')

    @unittest.skipUnless(sys.platform.startswith('darwin'), 'MacOs required')
    def test_only_mac(self):
        self.assertEqual(1, 1)

    # Описание ожидаемых ошибок:
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2, "broken")


@unittest.skip('showing class skipping')
class SkipTestCase(unittest.TestCase):
    def test_test(self):
        self.fail('error')
