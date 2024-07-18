dmg="11Medium armor"

def classification_of_armor(str):
    armor_class = ""
    if "Light armor" in str:
        armor_class = "Light armor"
    if "Medium armor" in str:
        armor_class = "Medium armor"
    if "Heavy armor" in str:
        armor_class = "Heavy armor"
    return armor_class

def dmg_calc(str):
    dmg_list = [int(i) for i in str.split() if i.isdigit()]
    dmg_int=dmg_list[0]


    dmg_reduction = 0
    if "Light armor" in str:
        dmg_reduction = dmg_int * 0.1
        for i in range(1,dmg_int):
            dmg_int -= 1
            if i >= dmg_int or i == 5:
                break
            if dmg_int == 0:
                break
        print(dmg_int)

    if "Medium armor" in str:
        dmg_reduction = dmg_int * 0.2
        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 8:
                break
            if dmg_int == 0:
                break
        print(dmg_int)

    if "Heavy armor" in str:
        dmg_reduction = dmg_int * (0.3)

        for i in range(1, dmg_int):
            dmg_int -= 1
            if i >= dmg_reduction or i == 12:
                break
            if dmg_int == 0:
                break
        print(dmg_int)
dmg_calc(dmg)