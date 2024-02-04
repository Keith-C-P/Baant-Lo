from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
import random
import os
import socket

Builder.load_file('main.kv')
class Client:
    def __init__(self, *args, **kwargs):
        address = kwargs.get('address')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((address, 9999))

    def send(self, *args, **kwargs):
        file_name = kwargs.get('file_name')
        if file_name:
            with open(file_name, 'rb') as file:
                file_type = os.path.splitext(file_name)[1]
                self.client.send(file_type.encode())
                data = file.read()
                self.client.sendall(data)
        self.client.send(b"<EOF>")

    def __del__(self):
        self.client.close()

class Server:
    def __init__(self, *args, **kwargs):
        address = kwargs.get('address')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((address, 9999))
        self.server.listen()
        self.conn, self.addr = self.server.accept()

    def receive(self, *args, **kwargs):
        self.file_type = self.conn.recv(1024).decode()
        self.file = open(f'file{self.file_type}', 'wb')
        self.file_bytes = b""
        self.done = False
        while not self.done:
            self.data = self.conn.recv(1024)
            if self.data[-5:] == b"<EOF>":
                self.done = True
                self.file_bytes = self.data[:-5]
            else:
                self.file_bytes += self.data
        self.file.write(self.file_bytes)
        self.file.close()

        return (str(f'file{self.file_type} saved'))

    def __del__(self):
        self.conn.close()
        self.server.close()

class HomeScreen(FloatLayout):
    uid = StringProperty('UID: ')
    pass
    

class ShareScreen(FloatLayout):
    def share(self):
        client = Client()
        client.send('share')

class Client(App):
    def on_start(self):
        self.root.uid += str(random.randint(0, 999999999)).zfill(9)

    def build(self):
        
        return HomeScreen()


if __name__ == '__main__':
    Client().run()