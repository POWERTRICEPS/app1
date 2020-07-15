from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
#from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self):
        self.manager.current = "welcome_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        print("yahoo!")

    def go_back(self):
        self.manager.current = "login_screen"


class HomeScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
