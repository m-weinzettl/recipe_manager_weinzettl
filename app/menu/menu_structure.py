def menu_user_input():
    menu = """
    Please choose an option:
    1. Alle Rezepte anzeigen
    2. Rezept hinzufügen (nicht implementiert)
    3. Rezept entfernen(nicht implementiert)
    4. Beenden
    """
    return menu

def menu_switch(option):
    if option == '1':
        return "Alle Rezepte anzeigen..."
    elif option == '2':
        return "Rezept hinzufügen..."
    elif option == '3':
        return "Rezept entfernen..."
    elif option == '4':
        return "Beenden..."
    else:
        return "Falsche Eingabe!."

def menu_loop():
    while True:
        print(menu_user_input())
        user_option = input("Wähle eine Option (1-4): ")
        result = menu_switch(user_option)
        print(result)
        if user_option == '4':
            break