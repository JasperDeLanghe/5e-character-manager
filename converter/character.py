from constants import PROFICIENCY_BONUS
from utils import calc_mod, calc_saving_throws, calc_skills


class Character:
    def __init__(self, data):
        self.data = data  # this is the non-derived data

        # This is all derived
        self.proficiency_bonus = PROFICIENCY_BONUS[data["level"]]
        self.ability_mods = {
            "strength": calc_mod(data["abilities"]["strength"]),
            "dexterity": calc_mod(data["abilities"]["dexterity"]),
            "constitution": calc_mod(data["abilities"]["constitution"]),
            "intelligence": calc_mod(data["abilities"]["intelligence"]),
            "wisdom": calc_mod(data["abilities"]["wisdom"]),
            "charisma": calc_mod(data["abilities"]["charisma"]),
        }
        self.skills = calc_skills(
            self.ability_mods,
            self.proficiency_bonus,
            data["skill_proficiencies"],
        )
        self.passive_perception = 10 + self.ability_mods["wisdom"]
        self.passive_insight = 10 + self.skills["insight"]
        self.passive_investigation = 10 + self.skills["investigation"]
        self.saving_throws = calc_saving_throws(
            self.ability_mods,
            self.proficiency_bonus,
            data["saving_throw_proficiencies"],
        )

    def __str__(self):
        return f"This character is {self.data["name"]}, a level {self.data["level"]} {self.data["race"]} {self.data["class"]}, with a proficiency bonus of {self.proficiency_bonus}"

    def get_name(self):
        return self.data["name"]
