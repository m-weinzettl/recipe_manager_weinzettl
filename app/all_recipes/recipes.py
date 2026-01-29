

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name={self.name}, ingredients={self.ingredients}, instructions={self.instructions})"

pasta = Recipe("Pasta", ["Nudeln, Fleisch"],
               ["wasser kochen", "Nudeln rein", "Fleisch anbraten"])
pizza = Recipe("Pizza", ["Teig, Tomatensauce, Käse"],
               ["Teig ausrollen", "Tomatensauce drauf", "Käse drauf", "backen"])
salad = Recipe("Salat", ["Blattsalat, Tomaten, Gurken"],
               ["Gemüse waschen", "Gemüse schneiden", "alles mischen"])




def show_ingredients(self):
    print(f"Zutaten für {self.name}:")
    for ingredient in self.ingredients:
        print(f"- {ingredient}")