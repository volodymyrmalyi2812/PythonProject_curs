# Створення списку
my_list = [1, 3, 6, 10]

# піднести кожен елемент до квадрату, використовуючи спискове включення
list_ = [x ** 2 for x in my_list]

# подібний механізм із генераторами:
# Вирази генератора укладені в круглі дужки ()
generator = (x ** 2 for x in my_list)

print(list_)
print(generator)
print(list(generator))
print(list(generator))

# [1, 9, 36, 100]
# <generator object <genexpr> at 0x7f5d4eb4bf50>
