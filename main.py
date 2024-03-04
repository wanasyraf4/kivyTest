# main.py

from kivy.app import App
from kivy.lang import Builder
from backend.logic import Backend

class MainApp(App):
    def build(self):
        self.backend = Backend()  # Initialize the backend
        return Builder.load_file('frontend/main.kv')

if __name__ == '__main__':
    MainApp().run()
