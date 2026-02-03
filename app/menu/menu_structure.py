from app.all_recipes.class_recipe import Recipe
from app.all_recipes.recipes_list import recipes
from app.all_recipes.search_recipe import search_menu
from app.services import recipe_service
from services.recipe_service import show_recipes_from_db, write_recipes_to_db
import json

def menu_user_input():
    return """
Bitte wählen Sie eine Option:
1. Alle Rezepte anzeigen
2. Rezept hinzufügen
3. Rezept suchen
4. Rezeptnamen ändern
5. ID anzeigen
6. Programm beenden
"""


def load_from_json(recipe_data_new):
    try:
        with open("./db_json.json", 'r', encoding='utf-8') as from_json:
            recipe_data_new = json.load(from_json)

        return recipe_data_new

    except FileNotFoundError:
        print("error")



def show_menu():
    recipe_data_new = {}
    recipe_data_new = load_from_json(recipe_data_new)


    while True:
        print(menu_user_input())
        user_option = input("Wählen Sie eine Option (1-4): ")

# alle rezepte anzeigen
        if user_option == '1':
            if not recipes:
                print("Kein Rezept gefunden.")
            else:
                show_recipes_from_db(recipe_data_new)

# neues rezept anlegen
        elif user_option == '2':
            new_recipe = Recipe()
            new_recipe.fill_recipe()

            write_recipes_to_db(new_recipe, recipe_data_new)

# rezept suchen / entfernen
        elif user_option == '3':
            search_menu(recipe_data_new)

        elif user_option == '4':
            recipe_service.edit_recipe(recipe_data_new)

# rezept id suchen
        elif user_option == '5':
            for name, book in recipe_data_new.items():
                print(f"\nRezept {name}: ID: {book['id']}")


#programm beenden
        elif user_option == '6':
            print("Programm beendet.")
            break

        else:
            print("Falsche Eingabe!")
