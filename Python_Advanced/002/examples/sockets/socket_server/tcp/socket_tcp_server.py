import socketserver


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request містить сокет клієнта, щоб ми могли відправити його повідомлення назад
        # (треба враховувати, що клієнт повинен вміти приймати повідомлення, відправивши йому назад повідомлення,
        # зовсім не означає, що він відразу його обробить - треба мати даний фукціонал)
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)


if __name__ == '__main__':
    # аналогічний приклад TCP-сервера та використання оператора with.
    with socketserver.TCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
