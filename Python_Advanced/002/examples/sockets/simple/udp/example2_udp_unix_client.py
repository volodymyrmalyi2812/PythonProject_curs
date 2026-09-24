# udp client
import socket

# створюємо UNIX UDP-сокет
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# відправляємо дані на UNIX-сокет-файл `unix.sock`
sock.sendto(b'Test Message', 'unix.sock')
