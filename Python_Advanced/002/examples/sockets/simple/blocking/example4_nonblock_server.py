import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# блокуючий режим, встановлюється для того, щоб ми не блокували інтерпретатор по вихові accept/recv якщо у нас мережа
# простоює. Приймає True/False.
sock.setblocking(False)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))
