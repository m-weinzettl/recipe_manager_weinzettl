
def data_validation_name():

    while True:
        name_input = input("Bitte geben Sie einen Rezeptnamen ein (max. 200 Zeichen: ")
        if 0 < len(name_input) <= 200:
            break
        else:
            print("Rezeptname zu lange. Bitte erneut eingeben")

    return name_input

def data_validation_ingredients():
    ingredient_input_new = []
    while True:
        ingredient_input = input("Zutaten (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
        if ingredient_input == '':
            break
        if 0 < len(ingredient_input) <= 100:
            ingredient_input_new.append(ingredient_input)
        else:
            print("Zutatenname zu lange. Bitte erneut eingeben")

    return ingredient_input_new


def data_validation_instructions():
    instructions_input_new = []
    while True:
        instructions_input = input("Anleitung (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
        if instructions_input == '':
            break
        if 0 < len(instructions_input) <= 100:
            instructions_input_new.append(instructions_input)
        else:
            print("Anleitung zu lange. Bitte erneut eingeben")

    return instructions_input_new