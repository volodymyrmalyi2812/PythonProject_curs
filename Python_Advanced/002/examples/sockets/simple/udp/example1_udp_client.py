# example 1 (UDP client socket )
import socket

# створюємо UDP socket (IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# відпраляємо повідомлення на `localhost:8888`
sock.sendto(b'Test message', ('localhost', 8888))
