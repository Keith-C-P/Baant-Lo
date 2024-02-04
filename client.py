import os
import socket

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 8010))

    def send(self, data):
        self.client.send(data.encode('utf-8'))
        response = self.client.recv(1024)
        print(response.decode('utf-8'))

    def __del__(self):
        self.client.close()



