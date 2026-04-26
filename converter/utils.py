import math
from constants import ABILITIES


def calc_mod(score):
    return math.floor((score - 10) / 2)


def get_ability_mods(data):
    mods = dict()

    for ability in ABILITIES:
        mods[ability] = calc_mod(data[ability])

    return mods


def calc_skills(mods, bonus, proficiencies):
    skills = {
        "acrobatics": mods[ABILITIES["DEX"]],
        "animal_handling": mods[ABILITIES["WIS"]],
        "arcana": mods[ABILITIES["INT"]],
        "athletics": mods[ABILITIES["STR"]],
        "deception": mods[ABILITIES["CHA"]],
        "history": mods[ABILITIES["INT"]],
        "insight": mods[ABILITIES["WIS"]],
        "intimidation": mods[ABILITIES["CHA"]],
        "investigation": mods[ABILITIES["INT"]],
        "medicine": mods[ABILITIES["WIS"]],
        "nature": mods[ABILITIES["INT"]],
        "perception": mods[ABILITIES["WIS"]],
        "performance": mods[ABILITIES["CHA"]],
        "persuasion": mods[ABILITIES["CHA"]],
        "religion": mods[ABILITIES["INT"]],
        "sleight_of_hand": mods[ABILITIES["DEX"]],
        "stealth": mods[ABILITIES["DEX"]],
        "survival": mods[ABILITIES["WIS"]],
    }

    for skill in skills:
        if skill in proficiencies:
            skills[skill] += bonus

    return skills


def calc_saving_throws(mods, bonus, proficiencies):
    abilities = {
        ABILITIES["STR"]: mods[ABILITIES["STR"]],
        ABILITIES["DEX"]: mods[ABILITIES["DEX"]],
        ABILITIES["CON"]: mods[ABILITIES["CON"]],
        ABILITIES["INT"]: mods[ABILITIES["INT"]],
        ABILITIES["WIS"]: mods[ABILITIES["WIS"]],
        ABILITIES["CHA"]: mods[ABILITIES["CHA"]],
    }

    print(abilities)
    print(mods)
    print(proficiencies)

    for ability in abilities:
        if ability in proficiencies:
            abilities[ability] += bonus

    return abilities
