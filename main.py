from kivy.app import App
from kivy.uix.widget import Widget

class Test(Widget):
    pass


class TestApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TestApp().run()