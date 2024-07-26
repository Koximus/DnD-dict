from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy

kivy.require('1.9.0')


class Armor:
    def __init__(self, armor_class, armor_type):
        self.armor_class = armor_class
        self.armor_type = armor_type


def set_armor_heavy(strin):
    Armor.armor_type = "Heavy"
    if "AC=" not in strin:
        return strin + " AC= "
    else:
        return strin


def set_armor_medium(strin):
    Armor.armor_type = "Medium"
    if "AC=" not in strin:
        return strin + " AC= "
    else:
        return strin


def set_armor_light(strin):
    Armor.armor_type = "Light"
    if "AC=" not in strin:
        return strin + " AC= "
    else:
        return strin


def set_armor_mage(strin):
    Armor.armor_type = "Mage"
    if "AC=" not in strin:
        return strin + " AC= "
    else:
        return strin


def dmg_calc(strin):
    if strin == "":
        return "ERROR"
    dmg_list = [int(i) for i in strin.split() if i.isdigit()]  # ez a buzi egy listát csinál...
    dmg_int = dmg_list[0]
    Armor.armor_class = dmg_list[1]

    if "AC=" not in strin:
        return "ERROR"

    if Armor.armor_type == "Light":
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_int*0.1 or i == Armor.armor_class/2:
                break
            if dmg_int == 0:
                break
        text = ("Sebzés: " + str(dmg_int))
        return text

    if Armor.armor_type == "Medium":
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_int*0.2 or i == Armor.armor_class/(3/4):
                break
            if dmg_int == 0:
                break
        text = ("Sebzés: " + str(dmg_int))
        return text

    if Armor.armor_type == "Heavy":
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_int*0.3 or i == Armor.armor_class:
                break
            if dmg_int == 0:
                break
        text = ("Sebzés: " + str(dmg_int))
        return text

    if Armor.armor_type == "Mage":
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_int*0.4 or i == Armor.armor_class:
                break
            if dmg_int == 0:
                break
        text = ("Sebzés: " + str(dmg_int))
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

    def set_armor_h(self):
        self.calc_field.text = set_armor_heavy(self.calc_field.text)

    def set_armor_m(self):
        self.calc_field.text = set_armor_medium(self.calc_field.text)

    def set_armor_l(self):
        self.calc_field.text = set_armor_light(self.calc_field.text)

    def set_armor_ms(self):
        self.calc_field.text = set_armor_mage(self.calc_field.text)


class NeuralCalc(App):
    def build(self):
        return MyRoot()


neuralcalc = NeuralCalc()
neuralcalc.run()
