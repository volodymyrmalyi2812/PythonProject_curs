import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # request містить дані та сокет-клієнт для комунікації
        data, socket = self.request
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    # використовуємо оператор with для створення сервера на 0:8888 та запускаємо with гарантує звільнення порту
    # та коректне завершення роботи серверу - у класу реалізований `__enter__` / `__exit__`.
    with socketserver.UDPServer(('0', 8888), EchoUDPHandler) as server:
        server.serve_forever()
