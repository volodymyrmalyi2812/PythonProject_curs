from task2 import calculate_bmi


assert round(calculate_bmi(70, 1.75), 2) == 22.86
assert round(calculate_bmi(80, 1.80), 2) == 24.69
assert round(calculate_bmi(50, 1.60), 2) == 19.53

try:
    calculate_bmi(-70, 1.75)
    assert False
except ValueError:
    assert True

try:
    calculate_bmi(70, -1.75)
    assert False
except ValueError:
    assert True

try:
    calculate_bmi(0, 1.75)
    assert False
except ValueError:
    assert True

try:
    calculate_bmi(70, 0)
    assert False
except ValueError:
    assert True

try:
    calculate_bmi("70", 1.75)
    assert False
except TypeError:
    assert True

try:
    calculate_bmi(70, "1.75")
    assert False
except TypeError:
    assert True

try:
    calculate_bmi("hello", "world")
    assert False
except TypeError:
    assert True

print("All assert tests passed")