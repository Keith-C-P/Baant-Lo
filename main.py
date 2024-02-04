from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
#from .client import Client
import random

Builder.load_file('main.kv')
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