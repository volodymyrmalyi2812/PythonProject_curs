# example 1 (UDP client socket )
import socket

# створюємо TCP сокет-клієнт
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# підключаємося до 8888 порту
sock.connect(('', 8888))
# відправляємо повідомлення
sock.send(b'Test message')
# закрываємо сокет-з'єднання
sock.close()
