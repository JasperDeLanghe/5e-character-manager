import yaml
from character import Character
from pypdf import PdfReader, PdfWriter

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
            "STR": character.data["abilities"]["strength"],
            "STRmod": character.ability_mods["strength"],
            "DEX": character.data["abilities"]["dexterity"],
            "DEXmod ": character.ability_mods["dexterity"],
            "CON": character.data["abilities"]["constitution"],
            "CONmod": character.ability_mods["constitution"],
            "INT": character.data["abilities"]["intelligence"],
            "INTmod": character.ability_mods["intelligence"],
            "WIS": character.data["abilities"]["wisdom"],
            "WISmod": character.ability_mods["wisdom"],
            "CHA": character.data["abilities"]["charisma"],
            "CHamod": character.ability_mods["charisma"],
            "Passive": character.passive_perception,
            # HP
            "HPMax": character.data["hit_points"],
            "HDTotal": f"{character.data['level']}{character.data["hit_dice"]}",
            # RP
            "PersonalityTraits ": character.data["personality_traits"],  # FIXME
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
            "ST Strength": character.saving_throws["strength"],
            "ST Dexterity": character.saving_throws["dexterity"],
            "ST Constitution": character.saving_throws["constitution"],
            "ST Intelligence": character.saving_throws["intelligence"],
            "ST Wisdom": character.saving_throws["wisdom"],
            "ST Charisma": character.saving_throws["charisma"],
            # "Check Box 11": "/Yes",  # str saving proficiency
            # "Check Box 18": "/Yes",  # dex saving proficiency
            # "Check Box 19": "/Yes",  # con saving proficiency
            # "Check Box 20": "/Yes",  # int saving proficiency
            # "Check Box 21": "/Yes",  # wis saving proficiency
            # "Check Box 22": "/Yes",  # cha saving proficiency
            # Currencies
            "CP": character.data["currency"]["cp"],
            "SP": character.data["currency"]["sp"],
            "EP": character.data["currency"]["ep"],
            "GP": character.data["currency"]["gp"],
            "PP": character.data["currency"]["pp"],
        },
        auto_regenerate=False,
    )

    writer.write("../filled.pdf")


if __name__ == "__main__":
    main()
