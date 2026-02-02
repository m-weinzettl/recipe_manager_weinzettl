from app.all_recipes.class_recipe import Recipe
from app.all_recipes.recipes_list import recipes

def menu_user_input():
    return """
Bitte wähle eine Option:
1. Alle Rezepte anzeigen
2. Rezept hinzufügen
3. Rezept entfernen (nicht implementiert)
4. Beenden
"""

def menu_loop():
    while True:
        print(menu_user_input())
        user_option = input("Wähle eine Option (1-4): ")

        if user_option == '1':
            if not recipes:
                print("Kein Rezept gefunden.")
            else:
                for name, data in recipes.items():
                    print(f"\nRezept {name}:")
                    print("Zutaten:")
                    for ingredient in data["ingredients"]:
                        print(f"- {ingredient}")
                    print("Anleitung:")
                    for instruction in data["instructions"]:
                        print(f"- {instruction}")

        elif user_option == '2':
            recipe = Recipe()
            recipe.fill_recipe()
            recipes[recipe.name] = {
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions
            }
            print("Rezept hinzugefügt.")

        elif user_option == '3':
            print("Funktion zum Entfernen noch nicht implementiert.")

        elif user_option == '4':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
