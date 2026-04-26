from enum import Enum

PROFICIENCY_BONUS = {
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 3,
    8: 3,
    9: 4,
    10: 4,
    11: 4,
    12: 4,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 6,
    18: 6,
    19: 6,
    20: 6,
}

ABILITIES = {
    "STR": "STR",
    "DEX": "DEX",
    "CON": "CON",
    "INT": "INT",
    "WIS": "WIS",
    "CHA": "CHA",
}


SPELLCASTING_ABILITY_BY_CLASS = {
    "Wizard": ABILITIES["INT"],
    "Artificer": ABILITIES["INT"],
    "Eldritch Knight": ABILITIES["INT"],
    "Fighter": ABILITIES["INT"],
    "Arcane Trickster": ABILITIES["INT"],
    "Rogue": ABILITIES["INT"],
    "Cleric": ABILITIES["WIS"],
    "Druid": ABILITIES["WIS"],
    "Ranger": ABILITIES["WIS"],
    "Monk": ABILITIES["WIS"],
    "Bard": ABILITIES["CHA"],
    "Paladin": ABILITIES["CHA"],
    "Sorcerer": ABILITIES["CHA"],
    "Warlock": ABILITIES["CHA"],
}
