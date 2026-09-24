'''
Завдання 1
Вивчіть основні поняття, розглянуті на уроці, а також особливості роботи з TCP та UDP протоколами в Python.
Завдання 2
Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. Він приймає повідомлення певного формату, де буде ідентифікатор пристрою, і друкує нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме унікальний ідентифікатор пристрою на сервер, повідомляючи про свою присутність.
Завдання 3
Створіть сокет, який приймає повідомлення з двома числами, що розділені комою. Сервер має конвертувати рядкове повідомлення у два числа й обчислювати його суму. Після успішного обчислення повертати відповідь клієнту.
Завдання 4
Вивчіть основні поняття, розглянуті в уроці, а також особливості роботи з HTTP-протоколами в Python, використовуючи бібліотеки urllib та requests.

Завдання 5

Вивчіть докладніше та спробуйте можливості налаштування pull з'єднань і його режимів. Використовуючи утиліту ab, протестуйте ваші напрацювання (https://ru.wikipedia.org/wiki/ApacheBench).

Завдання 6
Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та обробити відповіді. Необхідно попрактикуватися з urllib та бібліотекою requests. Рекомендується спочатку спробувати виконати запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests.
Завдання 7
Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та обмінюватися повідомленнями.
Завдання 8
Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний). Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та друкувати на консоль статус-код, заголовки та тіло відповіді.
'''




'''Завдання 1 
Вивчіть основні поняття, розглянуті на уроці, а також особливості роботи з TCP та UDP протоколами в Python.
'''


'''
Завдання 2
Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. 
Він приймає повідомлення певного формату, де буде ідентифікатор пристрою, і друкує нові під'єднання в консоль. 
Створіть UDP-клієнта, який надсилатиме унікальний ідентифікатор пристрою на сервер, повідомляючи про свою присутність.
'''
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(("127.0.0.1", 5000))
#
# devices = set()
#
# print("UDP сервер запущено")
#
# while True:
#     data, address = server.recvfrom(1024)
#     message = data.decode()
#
#     if message.startswith("DEVICE:"):
#         device_id = message.split(":", 1)[1]
#
#         if device_id not in devices:
#             devices.add(device_id)
#             print(f"Новий пристрій: {device_id}, адреса: {address}")
#
#         server.sendto(b"OK", address)


# import socket
# import uuid
#
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.settimeout(5)
#
# device_id = str(uuid.uuid4())
#
# message = f"DEVICE:{device_id}"
#
# client.sendto(message.encode(), ("127.0.0.1", 5000))
#
# try:
#     data, address = client.recvfrom(1024)
#     print("ID пристрою:", device_id)
#     print("Відповідь сервера:", data.decode())
# except socket.timeout:
#     print("Сервер не відповідає")
#
# client.close()


'''
Завдання 3
Створіть сокет, який приймає повідомлення з двома числами, що розділені комою. 
Сервер має конвертувати рядкове повідомлення у два числа й обчислювати його суму. 
Після успішного обчислення повертати відповідь клієнту
'''
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind(("127.0.0.1", 5001))
# server.listen()
#
# print("Сервер запущено")
#
# while True:
#     conn, address = server.accept()
#
#     with conn:
#         data = conn.recv(1024).decode()
#
#         try:
#             a, b = map(float, data.split(","))
#             result = a + b
#             response = str(result)
#         except ValueError:
#             response = "Помилка введення"
#
#         conn.sendall(response.encode())


# import socket
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", 5001))
#
# a = input("Перше число: ")
# b = input("Друге число: ")
#
# message = f"{a},{b}"
#
# client.sendall(message.encode())
#
# result = client.recv(1024).decode()
#
# print("Результат:", result)
#
# client.close()

'''
Завдання 4
Вивчіть основні поняття, розглянуті в уроці, а також особливості роботи з HTTP-протоколами в Python, використовуючи бібліотеки urllib та requests.
'''


'''
Завдання 5

Вивчіть докладніше та спробуйте можливості налаштування pull з'єднань і його режимів. Використовуючи утиліту ab, протестуйте ваші напрацювання
'''
# from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
#
#
# class Handler(BaseHTTPRequestHandler):
#     protocol_version = "HTTP/1.1"
#
#     def do_GET(self):
#         message = b"Hello, world!"
#
#         self.send_response(200)
#         self.send_header("Content-Type", "text/plain")
#         self.send_header("Content-Length", str(len(message)))
#         self.end_headers()
#
#         self.wfile.write(message)
#
#
# server = ThreadingHTTPServer(("127.0.0.1", 8000), Handler)
#
# print("HTTP сервер запущено")
#
# server.serve_forever()

# import requests
# from requests.adapters import HTTPAdapter
#
# session = requests.Session()
#
# adapter = HTTPAdapter(
#     pool_connections=10,
#     pool_maxsize=10,
#     pool_block=True
# )
#
# session.mount("http://", adapter)
#
# for i in range(10):
#     response = session.get("http://127.0.0.1:8000", timeout=5)
#     print(response.status_code, response.text)
#
# session.close()

'''
Завдання 6
Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та обробити відповіді. 
Необхідно попрактикуватися з urllib та бібліотекою requests. 
Рекомендується спочатку спробувати виконати запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests
'''
# import urllib.request
# import urllib.parse
# import json
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
#
# def request(method, url, data=None):
#     body = json.dumps(data).encode() if data is not None else None
#
#     req = urllib.request.Request(
#         url,
#         data=body,
#         headers={"Content-Type": "application/json"},
#         method=method
#     )
#
#     with urllib.request.urlopen(req, timeout=10) as response:
#         print("Статус:", response.status)
#         print(json.loads(response.read().decode()))
#
#
# request("GET", url + "/1")
#
# request("POST", url, {
#     "title": "My post",
#     "body": "Hello",
#     "userId": 1
# })
#
# request("PUT", url + "/1", {
#     "id": 1,
#     "title": "Updated post",
#     "body": "New text",
#     "userId": 1
# })
#
# request("PATCH", url + "/1", {
#     "title": "Changed title"
# })
#
# request("DELETE", url + "/1")
#
#
# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
#
# response = requests.get(url + "/1", timeout=10)
# print("GET:", response.status_code, response.json())
#
#
# response = requests.post(
#     url,
#     json={
#         "title": "My post",
#         "body": "Hello",
#         "userId": 1
#     },
#     timeout=10
# )
#
# print("POST:", response.status_code, response.json())
#
#
# response = requests.put(
#     url + "/1",
#     json={
#         "id": 1,
#         "title": "Updated post",
#         "body": "New text",
#         "userId": 1
#     },
#     timeout=10
# )
#
# print("PUT:", response.status_code, response.json())
#
#
# response = requests.patch(
#     url + "/1",
#     json={"title": "Changed title"},
#     timeout=10
# )
#
# print("PATCH:", response.status_code, response.json())
#
#
# response = requests.delete(url + "/1", timeout=10)
#
# print("DELETE:", response.status_code, response.text)


'''
Завдання 7
Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та обмінюватися повідомленнями
'''
# import socket
# import threading
#
# clients = []
# lock = threading.Lock()
#
#
# def broadcast(message, sender):
#     with lock:
#         for client in clients[:]:
#             if client != sender:
#                 try:
#                     client.sendall(message.encode())
#                 except OSError:
#                     clients.remove(client)
#
#
# def handle_client(client, address):
#     print(f"Підключився: {address}")
#
#     with lock:
#         clients.append(client)
#
#     try:
#         with client:
#             reader = client.makefile("r", encoding="utf-8")
#
#             for message in reader:
#                 broadcast(message, client)
#
#     except (ConnectionError, OSError):
#         pass
#
#     finally:
#         with lock:
#             if client in clients:
#                 clients.remove(client)
#
#         print(f"Відключився: {address}")
#
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind(("127.0.0.1", 5002))
# server.listen()
#
# print("Чат-сервер запущено")
#
# while True:
#     client, address = server.accept()
#
#     thread = threading.Thread(
#         target=handle_client,
#         args=(client, address),
#         daemon=True
#     )
#
#     thread.start()
#
#
#
# import socket
# import threading
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", 5002))
#
# name = input("Ваше ім'я: ")
#
#
# def receive():
#     try:
#         reader = client.makefile("r", encoding="utf-8")
#
#         for message in reader:
#             print(message, end="")
#
#     except (ConnectionError, OSError):
#         pass
#
#
# thread = threading.Thread(target=receive, daemon=True)
# thread.start()
#
# try:
#     while True:
#         message = input()
#
#         if message.lower() == "exit":
#             break
#
#         client.sendall(f"{name}: {message}\n".encode())
#
# except (KeyboardInterrupt, ConnectionError, OSError):
#     pass
#
# finally:
#     client.close()


'''
Завдання 8
Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний). 
Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та друкувати на консоль статус-код, заголовки та тіло відповіді
'''
# import requests
#
#
# def http_client(url, method, data=None):
#     try:
#         response = requests.request(
#             method=method.upper(),
#             url=url,
#             params=data if method.upper() == "GET" else None,
#             json=data if method.upper() != "GET" else None,
#             timeout=10
#         )
#
#         print("Статус-код:", response.status_code)
#         print("Заголовки:", dict(response.headers))
#         print("Тіло відповіді:", response.text)
#
#     except requests.RequestException as error:
#         print("Помилка:", error)
#
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
# http_client(url + "/1", "GET")
#
# http_client(url, "POST", {
#     "title": "Test",
#     "body": "Hello",
#     "userId": 1
# })
#
# http_client(url + "/1", "PUT", {
#     "title": "Updated",
#     "body": "New text",
#     "userId": 1
# })
#
# http_client(url + "/1", "PATCH", {
#     "title": "Changed"
# })
#
# http_client(url + "/1", "DELETE")