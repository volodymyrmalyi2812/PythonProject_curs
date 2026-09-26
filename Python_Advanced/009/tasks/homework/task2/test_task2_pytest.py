import pytest
from task2 import calculate_bmi


def test_bmi_1():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86


def test_bmi_2():
    assert round(calculate_bmi(80, 1.80), 2) == 24.69


def test_bmi_3():
    assert round(calculate_bmi(50, 1.60), 2) == 19.53


def test_negative_weight():
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)


def test_negative_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.75)


def test_zero_weight():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)


def test_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_text_weight():
    with pytest.raises(TypeError):
        calculate_bmi("70", 1.75)


def test_text_height():
    with pytest.raises(TypeError):
        calculate_bmi(70, "1.75")


def test_text_data():
    with pytest.raises(TypeError):
        calculate_bmi("hello", "world")