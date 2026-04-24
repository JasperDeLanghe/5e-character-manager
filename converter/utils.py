import math


def calc_mod(score):
    return math.floor((score - 10) / 2)


def calc_skills(mods, bonus, proficiencies):
    skills = {
        "acrobatics": mods["dexterity"],
        "animal_handling": mods["wisdom"],
        "arcana": mods["intelligence"],
        "athletics": mods["strength"],
        "deception": mods["charisma"],
        "history": mods["intelligence"],
        "insight": mods["wisdom"],
        "intimidation": mods["charisma"],
        "investigation": mods["intelligence"],
        "medicine": mods["wisdom"],
        "nature": mods["intelligence"],
        "perception": mods["wisdom"],
        "performance": mods["charisma"],
        "persuasion": mods["charisma"],
        "religion": mods["intelligence"],
        "sleight_of_hand": mods["dexterity"],
        "stealth": mods["dexterity"],
        "survival": mods["wisdom"],
    }

    for skill in skills:
        if skill in proficiencies:
            skills[skill] += bonus

    return skills


def calc_saving_throws(mods, bonus, proficiencies):
    abilities = {
        "strength": mods["strength"],
        "dexterity": mods["dexterity"],
        "constitution": mods["constitution"],
        "intelligence": mods["intelligence"],
        "wisdom": mods["wisdom"],
        "charisma": mods["charisma"],
    }

    for ability in abilities:
        if ability in proficiencies:
            abilities[ability] += bonus

    return abilities
