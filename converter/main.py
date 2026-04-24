import yaml
from character import Character

yaml_file = "../examples/pedro-salazar.yaml"


def main():
    with open(yaml_file, "r") as f:
        d = yaml.load(f, Loader=yaml.FullLoader)

    character = Character(d)
    print(character)


if __name__ == "__main__":
    main()
