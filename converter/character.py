from constants import PROFICIENCY_BONUS
from utils import calc_mod, calc_saving_throws, calc_skills


class Character:
    def __init__(self, data):
        self.__data = data  # this is the non-derived data

        # This is all derived
        self.__proficiency_bonus = PROFICIENCY_BONUS[data["level"]]
        self.__ability_mods = {
            "strength": calc_mod(data["abilities"]["strength"]),
            "dexterity": calc_mod(data["abilities"]["dexterity"]),
            "constitution": calc_mod(data["abilities"]["constitution"]),
            "intelligence": calc_mod(data["abilities"]["intelligence"]),
            "wisdom": calc_mod(data["abilities"]["wisdom"]),
            "charisma": calc_mod(data["abilities"]["charisma"]),
        }
        self.__skills = calc_skills(
            self.__ability_mods,
            self.__proficiency_bonus,
            data["skill_proficiencies"],
        )
        self.__passive_perception = 10 + self.__ability_mods["wisdom"]
        self.__passive_insight = 10 + self.__skills["insight"]
        self.__passive_investigation = 10 + self.__skills["investigation"]
        self.__saving_throws = calc_saving_throws(
            self.__ability_mods,
            self.__proficiency_bonus,
            data["saving_throw_proficiencies"],
        )

    def __str__(self):
        return f"This character is {self.__data["name"]}, a level {self.__data["level"]} {self.__data["race"]} {self.__data["class"]}, with a proficiency bonus of {self.__proficiency_bonus}"
