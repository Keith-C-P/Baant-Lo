from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Client(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a Label
        self.label = Label(text='Hello, Kivy!')

        # Create a Button
        btn = Button(text='Click Me!')
        btn.bind(on_press=self.on_button_click)

        # Add the Label and Button to the layout
        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        # Change the label text when the button is clicked
        self.label.text = 'Button On'


if __name__ == '__main__':
    Client().run()