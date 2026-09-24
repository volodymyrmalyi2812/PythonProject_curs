# example 1 (UDP server socket)
import socket

# створюємо UDP-сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# резервуємо порт 8888
sock.bind(('', 8888))
# читаємо 1024 байт
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
# закриваємо сокет
sock.close()
