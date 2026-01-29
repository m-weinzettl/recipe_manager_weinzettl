

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name={self.name}, ingredients={self.ingredients}, instructions={self.instructions})"

    def show_ingredients(self):
        print(f"Zutaten für {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def show_instructions(self):
        print(f"Anleitung für {self.name}:")
        for instruction in self.instructions:
            print(f"- {instruction}")