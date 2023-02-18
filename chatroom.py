import threading
import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096

CONN = (SERVER_HOST, SERVER_PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(CONN)
server.listen()
clients_list = []
names_list = []


class incoming_messages():
    def broadcast(message):
        for client in clients_list:
            client.send(message)

    def handle(client):
        while True:
            try:
                messege = client.recv(1024)
                incoming_messages.broadcast(messege)
            except:
                index = clients_list.index(client)
                clients_list.remove(client)
                client.close()
                nickname = names_list[index]
                incoming_messages.broadcast(f'{nickname} left the chart'.encode('ascii'))
                names_list.remove(nickname)
                break

    def receive(recieve1):
        print("server is running... ready for connections")
        while True:
            client, address = server.accept()
            print(f'connected with{str(address)}')
            clients_list.append(client)
            clients_list.index(client)
            client.send('connection available'.encode('ascii'))
            username = client.recv(1024).decode('ascii')
            names_list.append(username)

            print(f'the current connected device is  {username}')
            incoming_messages.broadcast(f'{username} joined the chart'.encode('ascii'))
            num = len(clients_list)
            print(num)
            client.send(f'{username}   you have successfully connected to the server'.encode('ascii'))
            incoming_messages.handle(client)
            try:
                thread = threading.Thread(target=incoming_messages.handle, args=client)
                thread.start()
            except:
                print('')
