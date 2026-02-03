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

