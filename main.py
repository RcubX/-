from kivymd.app import MDApp


from kivy.uix.gridlayout import GridLayout


from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy','keyboard_mode','systemanddock')

from kivymd.theming import ThemeManager

Window.size=(480,703)

def get_ingridients(m):
    nitro=str(round((m/3600),3))
    salt=str(round((m/60),4))
    dextrose=str(round((m/(3600*24)),5))
    starts=str(round((m/(3600*24*30)),6))
    salting_time=str(round((m/(3600*24*30*365)),7))

    return{'nitro': nitro,'salt':salt,'dextrose':dextrose,'starts':starts,
    'salting_time':salting_time}




class Conteiner(GridLayout):
    def calculate(self):
        try:
            mass=int(self.text_input.text)
        except :
            mass=0

        ingridients=get_ingridients(mass)

        self.salt.text=ingridients.get('salt')
        self.nitr.text=ingridients.get('nitro')
        self.dext.text=ingridients.get('dextrose')
        self.start.text=ingridients.get('starts')
        self.time.text=ingridients.get('salting_time')






class MyApp(MDApp):
    theme_cls=ThemeManager()
    title='Coppa app'
    def build(self):
        #self.theme_cls.theme_style="Dark"
        return Conteiner()



if __name__ == '__main__':
    MyApp().run()
