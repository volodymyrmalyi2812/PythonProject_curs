import gevent
from gevent.event import Event


def waiter():
    print('I am waiting for event')
    # очікування події з блокуванням подальшого виконання коду функції
    event.wait()
    print('Waiter done')


def emitter():
    print('Emitter is sleeping')
    # засинаємо на 3 секунди
    gevent.sleep(3)
    # встановлюємо подію
    event.set()
    print('I kill endless task!')
    # зупиняємо нескінченний greenlet примусово
    endless_task.kill()


def endless():
    while True:
        print('Endless Task will be working forever!')
        gevent.sleep(2)


# створюємо Event, який імпортували із модуля gevent.event
event = Event()

endless_task = gevent.spawn(endless)
jobs = [
    gevent.spawn(emitter),
    gevent.spawn(waiter),
    endless_task,
]


gevent.wait(jobs)
