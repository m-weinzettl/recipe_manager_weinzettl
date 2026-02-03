from app.all_recipes.class_recipe import Recipe
from app.all_recipes.recipes_list import recipes
from app.all_recipes.search_recipe import search_menu

def menu_user_input():
    return """
Bitte wählen Sie eine Option:
1. Alle Rezepte anzeigen
2. Rezept hinzufügen
3. Rezept suchen
4. ID anzeigen
5. Programm beenden
"""

def show_menu():
    while True:
        print(menu_user_input())
        user_option = input("Wählen Sie eine Option (1-4): ")

# alle rezepte anzeigen
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

# neues rezept anlegen
        elif user_option == '2':
            recipe = Recipe()
            recipe.fill_recipe()
            recipes[recipe.name] = {
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "id": recipe.get_id()
            }
            print("Rezept hinzugefügt.")

# rezept suchen / entfernen
        elif user_option == '3':
            search_menu()

# rezept id suchen
        elif user_option == '4':
            for name, book in recipes.items():
                print(f"\nRezept {name}: ID: {book['id']}")

#programm beenden
        elif user_option == '5':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
