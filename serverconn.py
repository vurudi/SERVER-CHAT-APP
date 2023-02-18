import socket
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

class connection:
        def conn(name):
                s = socket.socket()
                host = "192.168.56.1"
                port = 5001
                porthost=(host,port)
                return porthost