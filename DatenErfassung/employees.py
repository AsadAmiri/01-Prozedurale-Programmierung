# Leere Liste um Personendaten zu speichern
employees = []

# Endlose Schleife um Menü wiederholt zu zeigen
while True:

    # Try-except: Fehler abfangen, beim Umwandeln der Eingabe in eine Zahl(int),  wenn keine Zahl eingegeben wird.
    try:
        # Menü anzeigen
        print("1. Persondaten hinzufügen")
        print("2. Persondaten anzeigen")
        print("3. Progream beenden")
        user_choice = int(input("Ihre Eingabe: "))
    except ValueError:
        print("Ungültige Eingabe! 1, 2 oder 3 eingeben!")
        continue    # zurück zum Menü

    if user_choice == 1:
        # Vorname validieren und einlesen
        while True:
            first_name = input("Vorname eingeben: ")
            first_name = first_name.strip() # leer Zeichen vom Anfang/Ende entfernen
            # Uberprüfen ob nur Buchstaben eingegeben wurden, leer Zeichen erlaubt
            if first_name.replace(" ","").isalpha():
                break   # Schleife beenden wenn Eingabe gültig ist
            else:
                print("Eingabe ungültig, erneut versuchen!")
        # Nachname validieren und einlesen
        while True:
            last_name = input("Nachname eingeben: ")
            last_name = last_name.strip()   # leer Zeichen vom Anfang/Ende entfernen
            if last_name.replace(" ","").isalpha():
                break
            else:
                print("Eingabe ungültig, erneut versuchen!")

        # Geburtsdatum validieren
        while True:
            date_of_birth = input("Geburtsdatum eingeben TT.MM.JJJJ: ")
            date_of_birth = date_of_birth.strip()
            # Format von Geburtsdatum uberprüfen
            if(len(date_of_birth) != 10 or date_of_birth[2] != '.' or date_of_birth[5] != '.'):
                print("Datum müss in TT.MM.JJJJ Format eigegeben werden!")
                continue    # User erneut auffordern
            # mit try-except fehler abfangen
            try:
                # Geburtsdatum in Tag, Monat und Jahr teilen (split), ob tatsächlich Zahlen sind
                day = date_of_birth[0:2]
                month = date_of_birth[3:5]
                year = date_of_birth[6:10]
                day = int(day)
                month = int(month)
                year = int(year)
            except ValueError:
                print("Tag, Monat und Jahr müssen Zahlen sein!")
                continue
            # Jahr validieren
            if year > 2008 or year < 1925:
                print("Person müss zwischen 18 und 100 Jahre alt sein!")
                continue # wenn jünger als 18 oder älter als 100, erneute Eingabe auffordern
            # Monat validieren
            if month < 1 or month > 12:
                print("Monat müss zwischen 1 und 12 sein!")
                continue
            # Anzahl der Tagen in einem Monat festlegen
            months_with_30 = [4, 6, 9, 11] # April, Juni, September, November
            if month == 2:
                max_days = 28
            elif month in months_with_30:
                max_days = 30
            else:
                max_days = 31
            # Tagen validieren
            if day < 1 or day > max_days:
                print(f"Tag müss zwischen 1 und {max_days} für Monat {month} sein!")
                continue

            break # While-Schleife verlassen wenn alles validiert

        # Adresse validieren und einlesen
        while True:
            address = input("Adresse eingeben: ")
            address = address.strip()   # leer Zeichen vom Anfang/Ende entfernen
            # Variable: es müss mindestens eine Nummer (Hausnummer) vorhanden sein
            has_number = False
            for char in address:
                if char.isdigit():
                    has_number = True
                    break
            # Variable für Buchstaben, Zahlen und erlaubte Sonderzeichen in Adresse
            allowed_symbols = [' ', '-', ',', '/', '.']
            symbols = True
            for char in address:
                # Falls ein Zeichen nicht alphanumerisch und nicht in allowed_symbols ist,symbols auf False setzen
                if not (char.isalnum() or char in allowed_symbols):
                    symbols = False
            # prüfen ob, mindestens eine Zahl und nur Buchstaben/Zahlen, ob auch nur erlaubte Zeichen vorhanden sind
            if (has_number and (address.isalnum() or symbols)):
                break   # Schleife verlassen wenn gültige Adresse
            else:
                # sonst erneut eingeben
                print("Adresse ungültig, erneut versuchen!")


    #elif user_choice == 2:

    elif user_choice == 3:
        break

    else:
        print("Ungültige Eingabe! 1, 2 oder 3 eingeben!")
