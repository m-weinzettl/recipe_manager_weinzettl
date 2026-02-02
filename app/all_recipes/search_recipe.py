from app.all_recipes.recipes_list import recipes

def search_menu():
    print("""
Rezept suchen:
1. Rezeptname
2. Zutat
3. Abbrechen
""")

    while True:
        choice = input("Option auswählen?")
        if choice == "1":
            search_by_name()
        elif choice == "2":
            recipe_search_by_ingredient()
        elif choice == "3":
            break

def search_by_name():
    search_name = input("Bitte Rezeptname eingbene: ").lower()
    found = False

    for name, book in recipes.items():
        if search_name.lower() == name.lower():
            found = True
            print(f"Rezept {name} gefunden!")
            second_choice = input("Wollen Sie die Zutaten anzeigen. (y/n): ")
            if second_choice.lower() == "y":
                for ingredient in book["ingredients"]:
                    print(f" - {ingredient}")
            elif second_choice.lower() == "n":
                break
            else:
                break

    if not found:
        print("Kein Rezept gefunden.")

def recipe_search_by_ingredient():
    search_ingredient = input("Bitte Zutat eingeben: ").lower()
    found = False

    for name, book in recipes.items():
        for ingredient in book["ingredients"]:
            if search_ingredient == ingredient.lower():
                found = True
                print(f"Zutat '{ingredient}' im Rezept '{name}' gefunden!")
                second_choice = input("Wollen Sie das Rezept anzeigen? (y/n): ")
                if second_choice.lower() == "y":
                    print(f"\nRezept: {name}")
                    print("Zutaten:")
                    for ing in book["ingredients"]:
                        print(f" - {ing}")
                    print("Anleitung:")
                    for instr in book["instructions"]:
                        print(f" - {instr}")
                break  # nur diese Zutat, dann weiter mit dem nächsten Rezept

    if not found:
        print("Keine Rezepte mit dieser Zutat gefunden.")
