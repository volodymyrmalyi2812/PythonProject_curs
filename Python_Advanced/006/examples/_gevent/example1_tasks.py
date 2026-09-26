import gevent


def task():
    print('Gevent sleep')
    gevent.sleep(1)
    print('Gevent finished')


# поміщаємо функцію у гринлети
jobs = [
    gevent.spawn(task),
    gevent.spawn(task),
    gevent.spawn(task)
]

# блокуємо подальшу роботу програми та чекаємо на виконання всіх гринлетів
gevent.joinall(jobs)
