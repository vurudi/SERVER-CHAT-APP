import tqdm
import os
import socket
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

class FileTrancefar:
    def sendfile(name):
        s = socket.socket()
        host = "192.168.56.1"
        port = 5001
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected to ", host)
        filename = name  # SENDING MODULE
        filesize = os.path.getsize(filename)
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        # file = open(filename, 'wb')

        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True,
                             unit_divisor=1024)
        with open(filename, "rb") as f:
            tim = 0
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        print("file shared successfully")
        os.remove('respective file')
        s.close()

    def filerecv(self):
        s = socket.socket()
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(10)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        print("Waiting for the client to connect... ")
        client_socket, address = s.accept()
        print(f"[+] {address} is connected.")
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
                progress.update(len(bytes_read))
        client_socket.close()
        s.close()

