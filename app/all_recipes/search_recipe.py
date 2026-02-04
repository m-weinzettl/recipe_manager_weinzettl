
import json

def search_menu(recipe_data_new):
    print("""
Rezept suchen:
1. Rezeptname
2. Zutat
3. Rezept löschen
4. Abbrechen
""")

    while True:
        choice = input("Option auswählen?")
        if choice == "1":
            search_by_name()
        elif choice == "2":
            recipe_search_by_ingredient()
        elif choice == "3":
            recipe_data_new = delete_recipe(recipe_data_new)
        elif choice == "4":
            break

def search_by_name(recipe_data_new):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False

    for name, book in recipe_data_new.items():
        if search_name.lower() == name.lower():
            found = True
            print(f"Rezept {name} gefunden!")
            show = input("Wollen Sie die Zutaten anzeigen. (y/n): ")
            if show.lower() == "y":
                for ingredient in book["ingredients"]:
                    print(f" - {ingredient}")
            elif show.lower() == "n":
                break
            else:
                break

    if not found:
        print("Kein Rezept gefunden.")


def recipe_search_by_ingredient(recipe_data_new):
    search_ingredient = input("Bitte Zutat eingeben: ").lower()
    found = False

    for name, book in recipe_data_new.items():
        for ingredient in book["ingredients"]:
            if search_ingredient in ingredient.lower():
                found = True
                print(f"Zutat '{ingredient}' im Rezept '{name}' gefunden!")
                show = input("Rezept anzeigen? (y/n): ")
                if show.lower() == "y":
                    print(f"\nRezept: {name}")
                    print("Zutaten:")
                    for ing in book["ingredients"]:
                        print(f" - {ing}")
                    print("Anleitung:")
                    for instr in book["instructions"]:
                        print(f" - {instr}")
                break

    if not found:
        print("Keine Rezepte mit dieser Zutat gefunden.")


def delete_recipe(recipe_data_new):
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False
    recipe_found = None
    for name, book in recipe_data_new.items():
         if search_name.lower() == name.lower():
            recipe_found = name
            break

    print(f"Rezept {recipe_found} gefunden!")
    delete_yn = input("Wollen Sie das Rezept löschen?")
    if delete_yn.lower() == "y":
        del recipe_data_new[recipe_found]
    with open("./db_json.json", 'w', encoding='utf-8') as db:
        json.dump(recipe_data_new, db, ensure_ascii=False, indent=4)
        print(f"Rezept {recipe_found} gelöscht!")

    return recipe_data_new

