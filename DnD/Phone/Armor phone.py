from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy

kivy.require('1.9.0')

def dmg_calc(strin):
    dmg_list = [int(i) for i in strin.split() if i.isdigit()]       # ez a buzi egy listát csinál...
    dmg_int = dmg_list[0]

    if strin.count("armor") > 1:
        MyRoot.clear()

        return "ERROR"

    if "Light armor" in strin:
        dmg_reduction = dmg_int * 0.1
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 5:
                break
            if dmg_int == 0:
                break
        text = ("= " + str(dmg_int))
        return text

    if "Medium armor" in strin:
        dmg_reduction = dmg_int * 0.2
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 8:
                break
            if dmg_int == 0:
                break

        text = ("= " + str(dmg_int))
        return text

    if "Heavy armor" in strin:
        dmg_reduction = dmg_int * 0.3

        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 12:
                break
            if dmg_int == 0:
                break
        text = ("= " + str(dmg_int))

        return text
class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()
    def calc_symbol(self, symbol):
        self.calc_field.text += symbol
    def clear(self):
        self.calc_field.text = ""
    def get_result(self):
        self.calc_field.text = dmg_calc(self.calc_field.text)

class NeuralCalc(App):
    def build(self):
        return MyRoot()


neuralcalc=NeuralCalc()
neuralcalc.run()