from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random
from kivy.uix.popup import Popup

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def forgot_pass(self):
        self.manager.current = "forgot_password"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "welcome_screen"
            print("Hello")
        else:
            self.ids.login_wrong = "Wrong username or password."

class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        print("yahoo!")
        self.manager.current = "sign_up_screen_success"

    def go_back(self):
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    pass


class HomeScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = "up"
        self.manager.current = "login_screen"
    def campus_screen(self):
        self.manager.current = "campus_screen"
    def admission_screen(self):
        self.manager.current = "admission_screen"
    def mycourse_screen(self):
        self.manager.current = "mycourse_screen"
    def mygpa_screen(self):
        self.manager.current = "mygpa_screen"
    def ec_screen(self):
        self.manager.current = "ec_screen"
    def ucchance_screen(self):
        self.manager.current = "ucchance_screen"

class AppScreen(Screen):
    def go_back(self):
        self.manager.current = "home_screen"
    def go_here(self):
        self.manager.current = "login_screen"

class CampusScreen(AppScreen):
    pass
class AdmissionScreen(AppScreen):
    pass
class MyCourseScreen(AppScreen):
    pass

class MyGPAScreen(AppScreen):
    pass
class MyECScreen(AppScreen):
    pass
class UCChanceScreen(AppScreen):
    pass

class WelcomeScreen(AppScreen, Screen):
    pass

class ForgotPassword(AppScreen, Screen):
    pass

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
