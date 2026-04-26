import yaml
from character import Character
from pypdf import PdfReader, PdfWriter
from constants import ABILITIES

yaml_file = "../examples/pedro-salazar.yaml"
fillable_sheet = "../sheet.pdf"


def get_character():
    with open(yaml_file, "r") as f:
        d = yaml.load(f, Loader=yaml.FullLoader)

    return Character(d)


def checkbox(val, list):
    if val in list:
        return "/Yes"
    return "/No"


def main():
    character = get_character()
    # print(character)
    reader = PdfReader(fillable_sheet)
    writer = PdfWriter()

    fields = reader.get_fields()
    # print(fields)

    writer.append(reader)

    # page 1
    writer.update_page_form_field_values(
        writer.pages[0],
        {
            # Meta
            "CharacterName": character.data["name"],
            "ClassLevel": f"{character.data["class"]} - {character.data["level"]}",
            "Background": character.data["background"],
            "PlayerName": character.data["player"],
            "Race ": character.data["race"],
            "Alignment": character.data["alignment"],
            "XP": character.data["experience"],
            # Stats
            "ProfBonus": character.proficiency_bonus,
            "AC": character.data["armor_class"],
            "Initiative": character.data["initiative_bonus"],
            "Speed": character.data["speed"],
            # Abilities
            "STR": character.data[ABILITIES["STR"]],
            "STRmod": character.ability_mods[ABILITIES["STR"]],
            "DEX": character.data[ABILITIES["DEX"]],
            "DEXmod ": character.ability_mods[ABILITIES["DEX"]],
            "CON": character.data[ABILITIES["CON"]],
            "CONmod": character.ability_mods[ABILITIES["CON"]],
            "INT": character.data[ABILITIES["INT"]],
            "INTmod": character.ability_mods[ABILITIES["INT"]],
            "WIS": character.data[ABILITIES["WIS"]],
            "WISmod": character.ability_mods[ABILITIES["WIS"]],
            "CHA": character.data[ABILITIES["CHA"]],
            "CHamod": character.ability_mods[ABILITIES["CHA"]],
            "Passive": character.passive_perception,
            # HP
            "HPMax": character.data["hit_points"],
            "HDTotal": f"{character.data['level']}{character.data["hit_dice"]}",
            # RP
            "PersonalityTraits ": character.data["personality_traits"],
            "Bonds": character.data["bonds"],
            "Ideals": character.data["ideals"],
            "Flaws": character.data["flaws"],
            # Skills
            "Acrobatics": character.skills["acrobatics"],
            "Check Box 23": checkbox(
                "acrobatics", character.data["skill_proficiencies"]
            ),
            "Animal": character.skills["animal_handling"],
            "Check Box 24": checkbox(
                "animal_handling", character.data["skill_proficiencies"]
            ),
            "Arcana": character.skills["arcana"],
            "Check Box 25": checkbox("arcana", character.data["skill_proficiencies"]),
            "Athletics": character.skills["athletics"],
            "Check Box 26": checkbox(
                "athletics", character.data["skill_proficiencies"]
            ),
            "Deception ": character.skills["deception"],
            "Check Box 27": checkbox(
                "deception", character.data["skill_proficiencies"]
            ),
            "History ": character.skills["history"],
            "Check Box 28": checkbox("history", character.data["skill_proficiencies"]),
            "Insight": character.skills["insight"],
            "Check Box 29": checkbox("insight", character.data["skill_proficiencies"]),
            "Intimidation": character.skills["intimidation"],
            "Check Box 30": checkbox(
                "intimidation", character.data["skill_proficiencies"]
            ),
            "Investigation ": character.skills["investigation"],
            "Check Box 31": checkbox(
                "investigation", character.data["skill_proficiencies"]
            ),
            "Medicine": character.skills["medicine"],
            "Check Box 32": checkbox("medicine", character.data["skill_proficiencies"]),
            "Nature": character.skills["nature"],
            "Check Box 33": checkbox("nature", character.data["skill_proficiencies"]),
            "Perception ": character.skills["perception"],
            "Check Box 34": checkbox(
                "perception", character.data["skill_proficiencies"]
            ),
            "Performance": character.skills["performance"],
            "Check Box 35": checkbox(
                "performance", character.data["skill_proficiencies"]
            ),
            "Persuasion": character.skills["persuasion"],
            "Check Box 36": checkbox(
                "persuasion", character.data["skill_proficiencies"]
            ),
            "Religion": character.skills["religion"],
            "Check Box 37": checkbox("religion", character.data["skill_proficiencies"]),
            "SleightofHand": character.skills["sleight_of_hand"],
            "Check Box 38": checkbox(
                "sleight_of_hand", character.data["skill_proficiencies"]
            ),
            "Stealth ": character.skills["stealth"],
            "Check Box 39": checkbox("stealth", character.data["skill_proficiencies"]),
            "Survival": character.skills["survival"],
            "Check Box 40": checkbox("survival", character.data["skill_proficiencies"]),
            # Saving Throws
            "ST Strength": character.saving_throws[ABILITIES["STR"]],
            "ST Dexterity": character.saving_throws[ABILITIES["DEX"]],
            "ST Constitution": character.saving_throws[ABILITIES["CON"]],
            "ST Intelligence": character.saving_throws[ABILITIES["INT"]],
            "ST Wisdom": character.saving_throws[ABILITIES["WIS"]],
            "ST Charisma": character.saving_throws[ABILITIES["CHA"]],
            "Check Box 11": checkbox(
                ABILITIES["STR"], character.data["saving_throw_proficiencies"]
            ),  # str saving proficiency
            "Check Box 18": checkbox(
                ABILITIES["DEX"], character.data["saving_throw_proficiencies"]
            ),  # dex saving proficiency
            "Check Box 19": checkbox(
                ABILITIES["CON"], character.data["saving_throw_proficiencies"]
            ),  # con saving proficiency
            "Check Box 20": checkbox(
                ABILITIES["INT"], character.data["saving_throw_proficiencies"]
            ),  # int saving proficiency
            "Check Box 21": checkbox(
                ABILITIES["WIS"], character.data["saving_throw_proficiencies"]
            ),  # wis saving proficiency
            "Check Box 22": checkbox(
                ABILITIES["CHA"], character.data["saving_throw_proficiencies"]
            ),  # cha saving proficiency
            # Currencies
            "CP": character.data["currency"]["cp"],
            "SP": character.data["currency"]["sp"],
            "EP": character.data["currency"]["ep"],
            "GP": character.data["currency"]["gp"],
            "PP": character.data["currency"]["pp"],
        },
        auto_regenerate=False,
    )

    # page 2
    writer.update_page_form_field_values(
        writer.pages[1],
        {
            "CharacterName 2": character.data["name"],
            "Age": character.data["appearance"]["age"],
            "Height": character.data["appearance"]["height"],
            "Weight": character.data["appearance"]["weight"],
            "Eyes": character.data["appearance"]["eyes"],
            "Skin": character.data["appearance"]["skin"],
            "Hair": character.data["appearance"]["hair"],
            "Backstory": character.data["backstory"],
        },
        auto_regenerate=False,
    )

    # page 3
    writer.update_page_form_field_values(
        writer.pages[2],
        {
            "Spellcasting Class 2": character.data["class"],
            "SpellcastingAbility 2": character.spellcasting_ability,
            "SpellSaveDC  2": character.spell_save_dc,
            "SpellAtkBonus 2": character.spell_attack_bonus,
        },
        auto_regenerate=False,
    )

    writer.write("../filled.pdf")


if __name__ == "__main__":
    main()
