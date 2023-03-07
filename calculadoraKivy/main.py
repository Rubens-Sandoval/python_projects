from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["+","-","/","*"]
        self.lastOperator = None
        self.lastButton = None

        main_layout = BoxLayout(orientation = 'vertical')

        self.solution = TextInput(multiline = False,
                                  readonly = True,
                                  halign = 'right',
                                  font_size = 55)

        main_layout.add_widget(self.solution)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label,
                    pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text='=',
                               pos_hint={'center_x':0.5,'center_y':0.5})
        equals_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            # Limpar solution
            self.solution.text = ""
            return
        else:
            if current and (self.lastOperator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.lastButton = button_text
        self.lastOperator = self.lastButton in self.operators


    def on_solution(self, instance):
        text = self.solution.text

        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
        else:
            return


if __name__ == '__main__':
    app = MainApp()
    app.run()
