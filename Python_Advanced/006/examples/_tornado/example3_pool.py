import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.gen
from tornado.ioloop import IOLoop
from tornado.process import cpu_count

# створюємо pool потоків для обчислень, можна вказати будь-яку кількість
pool = ThreadPoolExecutor(cpu_count())


def sync_highload_task(password):
    for i in range(100_000):
        password = hashlib.sha256(password).hexdigest().encode()
    return password

# використовуючи декоратор, позначаємо нашу функцію як корутину
@tornado.gen.coroutine
def make_password(password) -> str:
    # очікуємо результату з pool-а потоків і переключаємося на іншу
    # до тих пір, поки не отримаємо результат
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )
    return hashed_password


@tornado.gen.coroutine
def test_cor():
    for i in range(1, 10):
        print('Sleep on {}'.format(i))
        # ми засинаємо і переключаємося на іншу співпрограму
        yield tornado.gen.sleep(i)
    return 2


@tornado.gen.coroutine
def multi():
    # очікуємо виконання кількох корутин за допомогою gen.multi
    result = yield tornado.gen.multi([
        test_cor(),
        make_password('test_pass')
    ])
    print(result)


# запуск корутин у циклі подій - event loop
IOLoop.current().run_sync(multi)
