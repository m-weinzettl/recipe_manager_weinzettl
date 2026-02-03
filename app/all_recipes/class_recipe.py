import uuid
import json

class Recipe:
    def __init__(self, name=None, ingredients=None, instructions=None, id=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.__id = id or uuid.uuid4()

## getter setter für python / kapselung /


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
        self.name = input("Bitte geben Sie einen Rezeptnamen ein: ")

        self.ingredients = []
        while True:
            ingredient = input("Zutaten (Leer Enter um zu Beenden): ")
            if ingredient == "":
                break
            self.ingredients.append(ingredient)

        self.instructions = []
        while True:
            instruction = input("Anleitung (Leer Enter um zu Beenden): ")
            if instruction == "":
                break
            self.instructions.append(instruction)

    def do_dict(self):
        return {
            "name": self.name,
            "ingredients":  self.ingredients,
            "instructions": self.instructions,
            "id": str(self.__id)}

