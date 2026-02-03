
import uuid

#E
class Recipe:
    def __init__(self, name=None, ingredients=None, instructions=None, id=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.__id = id or uuid.uuid4() #uniqe id for each recipe for db integration

    def get_id(self):
        return self.__id

    def show_ingredients(self):
        print(f"\nZutaten für {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def show_instructions(self):
        print(f"\nAnleitung für {self.name}:")
        for instruction in self.instructions:
            print(f"- {instruction}")

    def fill_recipe(self):
        while True:
            name_input = input("Bitte geben Sie einen Rezeptnamen ein (max. 200 Zeichen: ")
            if 0 < len(name_input) <= 200:
                self.name = name_input
                break
            else:
                print("Rezeptname zu lange. Bitte erneut eingeben")

        self.ingredients = []
        while True:
            ingredient_input = input("Zutaten (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
            if ingredient_input == '':
                break
            if 0 < len(ingredient_input) <= 100:
                self.ingredients.append(ingredient_input)
            else:
                print("Zutatenname zu lange. Bitte erneut eingeben")


        self.instructions = []
        while True:
            instruction_input = input("Anleitung (Leer Enter um zu Beenden)\n(Max 100 Zeichen): ")
            if instruction_input == '':
                break
            if 0 < len(instruction_input) <= 100:
                self.instructions.append(instruction_input)
            else:
                print("Anelitungsschritt zu lange. Bitte erneut eingeben")

#code edit for json export
    def do_dict(self):
        return {
            "name": self.name,
            "ingredients":  self.ingredients,
            "instructions": self.instructions,
            "id": str(self.__id)}

