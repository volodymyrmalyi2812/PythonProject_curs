import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 255.255.255.255
sock.bind(('127.0.0.1', 8888))
# вказуємо чергу у 5 з'єднань, кількість клієнтів, які зможуть підключитися до сервера одночасно.
sock.listen(5)
# встановлюємо, щоб змогли відправляти широкомовні пакети на кілька адрес, наприклад: 255.255.255.255.
# Тоді ми надішлемо повідомлення на кілька клієнтів одночасно. називається широкомовним.
# Виключаємо можливість помилки, щоб ми не надсилали повідомлення випадково.
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) встановлюємо, щоб змогли перевикористовувати дані
# socket без інтервалів
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# беремо клієнта та його адресу
client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))
