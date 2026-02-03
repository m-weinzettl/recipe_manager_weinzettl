import json
import app.all_recipes.class_recipe as recipe_class

def show_recipes_from_db(recipe_data_new):

        for name, book in recipe_data_new.items():
            print(f"\nRezept {name}:")
            print("Zutaten:")
            for ingredient in book["ingredients"]:
                print(f"- {ingredient}")
            print("Anleitung:")
            for instruction in book["instructions"]:
                print(f"- {instruction}")

def write_recipes_to_db(new_recipe_data, recipe_data_new):

    recipe_data_new[new_recipe_data.name] = new_recipe_data.do_dict()

    with open("./db_json.json", 'w', encoding='utf-8') as db:
        json.dump(recipe_data_new, db, ensure_ascii=False, indent=4)
        print(f"Rezept {new_recipe_data.name}: Erfolgreich gespeichert")

def edit_recipe(recipe_data_new):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False
    recipe_found = None
    for name, book in recipe_data_new.items():
         if search_name.lower() == name.lower():
            recipe_found = name
            break
    if recipe_found:
        print(f"Rezept {recipe_found} gefunden!")
        edit_yn = input("Wollen Sie den Rezeptnamen ändern?")

        if edit_yn.lower() == "y":
            new_name = input("Bitte neuen Rezeptnamen eingeben.")

            book = recipe_data_new.pop(recipe_found)
            recipe_data_new[new_name] = book

            with open("./db_json.json", 'w', encoding='utf-8') as db:
                json.dump(recipe_data_new, db, ensure_ascii=False, indent=4)
                print(f"Rezept {recipe_found} geändert!")

    return recipe_data_new
