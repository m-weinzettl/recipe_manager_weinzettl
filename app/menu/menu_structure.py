from app.all_recipes.class_recipe import Recipe
from app.all_recipes.recipes_list import recipes

def menu_user_input():
    return """
Bitte wähle eine Option:
1. Alle Rezepte anzeigen
2. Rezept hinzufügen
3. Funktion zum Entfernen noch nicht implementiert
4. ID anzeigen
5. Rezept entfernen (nicht implementiert)
6. Beenden
"""

def show_menu():
    while True:
        print(menu_user_input())
        user_option = input("Wähle eine Option (1-4): ")

        if user_option == '1':
            if not recipes:
                print("Kein Rezept gefunden.")
            else:
                for name, book in recipes.items():
                    print(f"\nRezept {name}:")
                    print("Zutaten:")
                    for ingredient in book["ingredients"]:
                        print(f"- {ingredient}")
                    print("Anleitung:")
                    for instruction in book["instructions"]:
                        print(f"- {instruction}")

        elif user_option == '2':
            recipe = Recipe()
            recipe.fill_recipe()
            recipes[recipe.name] = {
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "id": recipe.id
            }
            print("Rezept hinzugefügt.")

        elif user_option == '3':
            print("Funktion zum Entfernen noch nicht implementiert.")

        elif user_option == '4':
            for name, book in recipes.items():
                print(f"\nRezept {name}: ID: {book['id']}")

        elif user_option == '5':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
