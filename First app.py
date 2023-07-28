from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CustomApp(App):
    def build(self):
        # Oyna joylashishi uchun BoxLayout obyekti
        layout = BoxLayout(orientation='vertical')

        # Matnni o'zgartirish uchun tugmalar
        self.button1 = Button(text='Tugma 1', on_press=self.on_button_press)
        self.button2 = Button(text='Tugma 2', on_press=self.on_button_press)
        self.button3 = Button(text='Tugma 3', on_press=self.on_button_press)

        # Tugmalarni oynaga qo'shish
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)

        return layout

    def on_button_press(self, button):
        # Tugma bosilganda tekstini o'zgartirish
        if button == self.button1:
            button.text = 'Birinchi tugma bosildi'
        elif button == self.button2:
            button.text = 'Ikkinchi tugma bosildi'
        elif button == self.button3:
            button.text = 'Uchinchi tugma bosildi'

if __name__ == '__main__':
    CustomApp().run()
