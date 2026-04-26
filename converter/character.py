from constants import PROFICIENCY_BONUS, SPELLCASTING_ABILITY_BY_CLASS, ABILITIES
from utils import get_ability_mods, calc_saving_throws, calc_skills


class Character:
    def __init__(self, data):
        self.data = data  # this is the non-derived data

        # This is all derived
        self.proficiency_bonus = PROFICIENCY_BONUS[data["level"]]
        self.ability_mods = get_ability_mods(self.data)
        self.skills = calc_skills(
            self.ability_mods,
            self.proficiency_bonus,
            data["skill_proficiencies"],
        )
        self.passive_perception = 10 + self.ability_mods[ABILITIES["WIS"]]
        self.passive_insight = 10 + self.skills["insight"]
        self.passive_investigation = 10 + self.skills["investigation"]
        self.saving_throws = calc_saving_throws(
            self.ability_mods,
            self.proficiency_bonus,
            data["saving_throw_proficiencies"],
        )
        self.spellcasting_ability = SPELLCASTING_ABILITY_BY_CLASS[self.data["class"]]
        self.spell_save_dc = (
            8 + self.proficiency_bonus + self.ability_mods[self.spellcasting_ability]
        )
        self.spell_attack_bonus = (
            self.proficiency_bonus + self.ability_mods[self.spellcasting_ability]
        )

    def __str__(self):
        return f"This character is {self.data["name"]}, a level {self.data["level"]} {self.data["race"]} {self.data["class"]}, with a proficiency bonus of {self.proficiency_bonus}"

    def get_name(self):
        return self.data["name"]
