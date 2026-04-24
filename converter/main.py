import yaml
from character import Character
from pypdf import PdfReader, PdfWriter

yaml_file = "../examples/pedro-salazar.yaml"
fillable_sheet = "../sheet.pdf"


def get_character():
    with open(yaml_file, "r") as f:
        d = yaml.load(f, Loader=yaml.FullLoader)

    return Character(d)


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
            "Animal": character.skills["animal_handling"],
            "Arcana": character.skills["arcana"],
            "Athletics": character.skills["athletics"],
            "Deception ": character.skills["deception"],
            "History ": character.skills["history"],
            "Insight": character.skills["insight"],
            "Intimidation": character.skills["intimidation"],
            "Investigation ": character.skills["investigation"],
            "Medicine": character.skills["medicine"],
            "Nature": character.skills["nature"],
            "Perception ": character.skills["perception"],
            "Performance": character.skills["performance"],
            "Persuasion": character.skills["persuasion"],
            "Religion": character.skills["religion"],
            "SleightofHand": character.skills["sleight_of_hand"],
            "Stealth ": character.skills["stealth"],
            "Survival": character.skills["survival"],
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
