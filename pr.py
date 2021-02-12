from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
 
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(250, 250))
        s.add_widget(fl)
        fl.add_widget(Button(
            text="Это кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0,35,44],
            background_normal='',
            size_hint=(.5, .25),
            pos=(910/2-160, 910/2-160)));
        fl.add_widget(Button(
            text="Кнопка 2",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1,0,0],
            background_normal='',
            size_hint=(.5, .25),
            pos=(1200/2-160, 910/2-160)));
        return s
    def btn_press(self, instance):        
        instance.text='Не нажимай'
        
if __name__=="__main__":
    myApp().run()
