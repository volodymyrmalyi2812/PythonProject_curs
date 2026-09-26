import unittest
from task2 import calculate_bmi


class TestBMI(unittest.TestCase):

    def test_bmi_1(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_bmi_2(self):
        self.assertAlmostEqual(calculate_bmi(80, 1.80), 24.69, places=2)

    def test_bmi_3(self):
        self.assertAlmostEqual(calculate_bmi(50, 1.60), 19.53, places=2)

    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)

    def test_zero_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_text_weight(self):
        with self.assertRaises(TypeError):
            calculate_bmi("70", 1.75)

    def test_text_height(self):
        with self.assertRaises(TypeError):
            calculate_bmi(70, "1.75")

    def test_text_data(self):
        with self.assertRaises(TypeError):
            calculate_bmi("hello", "world")


if __name__ == "__main__":
    unittest.main()