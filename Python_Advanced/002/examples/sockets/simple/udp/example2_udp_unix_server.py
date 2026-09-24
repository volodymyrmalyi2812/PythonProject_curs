# example 2 (UDP unix socket)
import os
import socket

unix_sock_name = 'unix.sock'
# створюємо UNIX UDP-сокет
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

# прив'язуємо socket-file методом `bind` для unix сокет метод приймає назву файлу.
sock.bind(unix_sock_name)

# нескінченний цикл для постійного читання даних
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))
