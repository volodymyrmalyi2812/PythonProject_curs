"""
Використання генераторів є чудовим способом оптимізації пам'яті.
Розглянемо приклад із зведенням числа у квадрат та перевіримо розмір отриманих об'єктів.

Можемо зробити це за допомогою функції sys.getsizeof():
"""
import sys
nums_lc = [i ** 2 for i in range(1000000)]
print(sys.getsizeof(nums_lc))

nums_gc = (i ** 2 for i in range(1000000))
print(sys.getsizeof(nums_gc))
