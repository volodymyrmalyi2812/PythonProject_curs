'''
Завдання 1

Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

Завдання 2

Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення списку, додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

Завдання 3

Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
'''


'''
Завдання 1

Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
'''

# iterable = [10, 20, 30, 40, 50]
#
# iterator = iter(iterable)
#
# while True:
#     try:
#         value = next(iterator)
#         print(value)
#
#     except StopIteration:
#         break


'''
Завдання 2

Взявши за основу код прикладу example_5.py, 
розширте функціональність класу MyList, 
додавши методи очищення списку, додавання елемента у довільне місце списку, 
видалення елемента з кінця та довільного місця списку.
'''


"""
Пример реализации списка с итератором
"""


class MyList(object):

    class _ListNode(object):

        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    class _Iterator(object):

        def __init__(self, list_instance):
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец"""

        node = MyList._ListNode(element)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node

        self._length += 1

    def clear(self):
        """Очистка списка"""

        self._head = None
        self._tail = None
        self._length = 0

    def insert(self, index, element):
        """Добавление элемента по индексу"""

        if index < 0 or index > self._length:
            raise IndexError('Неправильный индекс')

        # Добавление в конец
        if index == self._length:
            self.append(element)

        # Добавление в начало
        elif index == 0:
            node = MyList._ListNode(element)

            node.next = self._head
            self._head.prev = node
            self._head = node

            self._length += 1

        # Добавление в середину
        else:
            current_node = self._head

            for i in range(index):
                current_node = current_node.next

            node = MyList._ListNode(element)

            node.prev = current_node.prev
            node.next = current_node

            current_node.prev.next = node
            current_node.prev = node

            self._length += 1

    def pop(self):
        """Удаление последнего элемента"""

        if self._length == 0:
            raise IndexError('Список пустой')

        deleted_value = self._tail.value

        # Если в списке один элемент
        if self._length == 1:
            self._head = None
            self._tail = None

        # Если элементов несколько
        else:
            self._tail = self._tail.prev
            self._tail.next = None

        self._length -= 1

        return deleted_value

    def remove(self, index):
        """Удаление элемента по индексу"""

        if index < 0 or index >= self._length:
            raise IndexError('Неправильный индекс')

        # Удаление последнего элемента
        if index == self._length - 1:
            return self.pop()

        current_node = self._head

        for i in range(index):
            current_node = current_node.next

        deleted_value = current_node.value

        # Удаление первого элемента
        if index == 0:
            self._head = self._head.next
            self._head.prev = None

        # Удаление из середины
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

        self._length -= 1

        return deleted_value

    def __len__(self):
        return self._length

    def __repr__(self):
        result = 'MyList(['
        first_element = True

        for element in self:
            if first_element is False:
                result += ', '

            result += str(element)
            first_element = False

        result += '])'

        return result

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError('Неправильный индекс')

        node = self._head

        for i in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    my_list = MyList([1, 2, 5])

    print('Начальный список:')
    print(my_list)

    my_list.insert(2, 3)
    print('После добавления 3 на индекс 2:')
    print(my_list)

    my_list.pop()
    print('После удаления последнего элемента:')
    print(my_list)

    my_list.remove(1)
    print('После удаления элемента с индексом 1:')
    print(my_list)

    my_list.clear()
    print('После очистки:')
    print(my_list)


if __name__ == '__main__':
    main()



'''
Завдання 3

Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
'''


class ReverseIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.iterable[self.index]
        self.index -= 1

        return value


iterable = [1, 2, 3, 4, 5]

iterator = ReverseIterator(iterable)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break