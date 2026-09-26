from twisted.internet import reactor, defer


def resolve_deferred(deff, value):
    """
    Функція аналогічна прикладу example6_event_loop.py, де ми створювали футур,
    чекаючи результату в одній корутині, а встановлювали йому результат
    інший.
    """
    try:
        # callback аналогічний set_result
        deff.callback(value)
    except Exception as e:
        deff.errback(e)


def make_data(raw, timeout):
    print('make data called')
    # Використовуючи фреймворк twisted, створюємо deferred, він аналогічний Future.
    deferred = defer.Deferred()  # Future()
    # додаємо в цикл подій завдання до виконання
    reactor.callLater(
        timeout,
        resolve_deferred,
        deferred,
        raw
    )  # Future.set_result
    return deferred


def pipe_1(result):
    print('Logging value: {}'.format(result))
    return result


def pipe_2(result):
    return result + 10


def pipe_3(result):
    return result * 2


def pipe_4(result):
    return 100 / result


def error_1(e):
    print('Error: {}'.format(e))


deferred = make_data(40, 2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_3)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_4)
deferred.addCallbacks(pipe_1, error_1)

deferred = make_data(-10, 2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_3)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_4)
deferred.addCallbacks(pipe_1, error_1)

# додаємо завдання зупинення циклу подій через 4 сек.
reactor.callLater(4, reactor.stop)

print('Reactor is starting.')
# запускаємо цикл подій
reactor.run()
print('Reactor is stopped.')
