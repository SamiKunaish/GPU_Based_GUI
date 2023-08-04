from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

x = []
y = []

for i in range(1000000):
    x.append(i)
    y.append(i * i)

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

class Test(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class TestApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TestApp().run()