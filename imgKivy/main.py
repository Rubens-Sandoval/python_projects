from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        imgsDir = ['venv/imgs/pikachu.png', 'venv/imgs/muppet.png', 'venv/imgs/brain.png']

        for i in imgsDir:
            img = Image(source = i,
                             size_hint = (.5, .5),
                             pos_hint = {'center_x' : .5, 'center_y':.5})
            layout.add_widget(img)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
