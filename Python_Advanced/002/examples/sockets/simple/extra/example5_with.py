# with operator
import socket

# __enter__ / __exit__
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# можна використовувати оператор with, що гарантує закриття сокету у разі помилки або успішного виходу з циклу
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('8888 is bind')
    sock.bind(('127.0.0.1', 8888))

    while True:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))
