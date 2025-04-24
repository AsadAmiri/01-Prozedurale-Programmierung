# Leere Liste um Personendaten zu speichern
employees = []

# Endlose Schleife um Menü wiederholt zu zeigen
while True:
    try:
        # Menü anzeigen
        print("1. Persondaten hinzufügen")
        print("2. Persondaten anzeigen")
        print("3. Progream beenden")
        user_choice = int(input("Ihre Eingabe: "))

    except ValueError:
        print("Ungültige Eingabe! 1, 2 oder 3 eingeben!")
        continue

    if user_choice == 1:
        # Vorname validieren und einlesen
        while True:
            first_name = input("Vorname eingeben: ")
            if(first_name.strip().replace(" ","").isalpha()):
                break
            else:
                print("Eingabe ungültig, erneut versuchen!")
        # Nachname validieren und einlesen
        while True:
            last_name = input("Nachname eingeben: ")
            if(last_name.strip().replace(" ","").isalpha()):
                break
            else:
                print("Eingabe ungültig, erneut versuchen!")
        # Adresse validieren und einlesen
        while True:
            adresse = input("Straße und Hausnummer eingeben: ")
            # if(adresse.strip().isalnum() and any(char.isdigit() for char in adresse)):
            if (adresse.strip().replace(" ", "").isalnum()):
                break
            else:
                print("Adresse ungültig, erneut versuchen!")


    elif user_choice == 3:
        break
    else:
        print("Ungültige Eingabe! 1, 2 oder 3 eingeben!")
