import random


class Character:
    def __init__(self, race, role, stats):

        self.race = race
        self.role = role
        self.stats = stats

stats_dict = {}
def statdobas():
    stat = []
    stat.append(random.randint(1,6))
    stat.append(random.randint(1, 6))
    stat.append(random.randint(1, 6))
    stat.append(random.randint(1, 6))
    stat.sort()
    stat.pop(0)
    statszam=stat[0]+stat[1]+stat[2]
    return statszam
print(statdobas())
statoklistája= []
def osszes_stat_dobas():


    statoklistája.append(statdobas())
    statoklistája.append(statdobas())
    statoklistája.append(statdobas())
    statoklistája.append(statdobas())
    statoklistája.append(statdobas())
    statoklistája.append(statdobas())
    statoklistája.sort()
    return statoklistája



def statok_elosztasa(list):
    if Character.role = "Fighter" or "Barbarian":
        stats_dict = {"STR":statoklistája[5],"DEX":statoklistája[3],"CON":statoklistája[4],"WIS":statoklistája[2],"INT":statoklistája[0],"CHA":statoklistája[1]}
    if Character.role = "Rouge" :
        stats_dict = {"STR": statoklistája[3], "DEX": statoklistája[5], "CON": statoklistája[4],
                      "WIS": statoklistája[1], "INT": statoklistája[0], "CHA": statoklistája[2]}

    if Character.role = "Monk" or "Ranger":
        stats_dict = {"STR":statoklistája[2],"DEX":statoklistája[5],"CON":statoklistája[3],
                      "WIS":statoklistája[4],"INT":statoklistája[0],"CHA":statoklistája[1]}

    if Character.role = "Druid" :
        stats_dict = {"STR":statoklistája[2],"DEX":statoklistája[3],"CON":statoklistája[4],
                      "WIS":statoklistája[5],"INT":statoklistája[0],"CHA":statoklistája[1]}

    if Character.role = "Cleric":
        stats_dict = {"STR":statoklistája[5],"DEX":statoklistája[3],"CON":statoklistája[4],
                      "WIS":statoklistája[2],"INT":statoklistája[0],"CHA":statoklistája[1]}

    if Character.role = "Wizard":
        stats_dict = {"STR":statoklistája[0],"DEX":statoklistája[1],"CON":statoklistája[4],
                      "WIS":statoklistája[3],"INT":statoklistája[5],"CHA":statoklistája[2]}

    if Character.role = "Bard" or "Warlock" or "Sorcerer":
        stats_dict = {"STR":statoklistája[0],"DEX":statoklistája[3],"CON":statoklistája[4],
                      "WIS":statoklistája[2],"INT":statoklistája[1],"CHA":statoklistája[5]}




def set_character_class_Fighter():
    Character.role = "Fighter"


def set_character_class_Barbarian():
    Character.role = "Barbarian"

def set_character_class_Rouge():
    Character.role = "Rouge"

def set_character_class_Monk():
    Character.role = "Monk"

def set_character_class_Ranger():
    Character.role = "Ranger"

def set_character_class_Cleric():
        Character.role = "Cleric"

def set_character_class_Wizard():
        Character.role = "Wizard"

def set_character_class_Sorcerer():
        Character.role = "Sorcerer"

def set_character_class_Bard():
        Character.role = "Bard"

def set_character_class_Warlock():
        Character.role = "Warlock"
