import json
import app.all_recipes.class_recipe as recipe_class

def show_recipes_from_db():
    try:
        with open("./db_json.json", 'r', encoding='utf-8') as db:
            recipe_data = json.load(db)
            for name, book in recipe_data.items():
                print(f"\nRezept {name}:")
                print("Zutaten:")
                for ingredient in book["ingredients"]:
                    print(f"- {ingredient}")
                print("Anleitung:")
                for instruction in book["instructions"]:
                    print(f"- {instruction}")
    except FileNotFoundError:
        print("Die Datenbank wurde nicht gefunden.")
    except json.decoder.JSONDecodeError:
        print("Die Datei ist leer oder beschädigt.")

def write_recipes_to_db(new_recipe_data):
    file_path = "./db_json.json"

    try:
        with open("./db_json.json", 'r', encoding='utf-8') as db:
            recipe_data = json.load(db)
    except FileNotFoundError:
        print("Die Datenbank wurde nicht gefunden.")
    except json.decoder.JSONDecodeError:
        print("Die Datei ist leer oder beschädigt.")

    recipe_data[new_recipe_data.name] = new_recipe_data.do_dict()

    try:
        with open("./db_json.json", 'w', encoding='utf-8') as db:
            json.dump(recipe_data, db, ensure_ascii=False, indent=4)
            print(f"Rezept {new_recipe_data.name}: Erfolgreich gespeichert")

    except FileNotFoundError:
        print("Error")
    except json.decoder.JSONDecodeError:
        print("Error")

