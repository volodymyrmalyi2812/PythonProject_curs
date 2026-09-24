import socketserver


# даний приклад показує використання `ThreadingMixIn` для кожного нового клієнта, даний приклад використовується у
# фреймворку django для реалізації сервера розробки, щоб працювати з окремим клієнтом в окремому потоці.
class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)


if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
