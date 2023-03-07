from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(text = 'Hello World',
                      size_hint =(.5,.5),
                      pos_hint = {'center_x' : .5, 'center_y' : .5})

        btn.bind(on_press = self.on_press_button)
        return btn

    def on_press_button(self, instance):
        print('Você apertou o botão!')


if __name__ == '__main__':
    app = MainApp()
    app.run()
