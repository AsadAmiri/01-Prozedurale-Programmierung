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
            if not first_name:
                print("Vorname-Feld darf nicht leer sein!")
                continue
            # Uberprüfen ob nur Buchstaben eingegeben wurden, leer Zeichen erlaubt
            if first_name.replace(" ","").isalpha():
                break   # Schleife beenden wenn Eingabe gültig ist
            else:
                print("Eingabe ungültig, erneut versuchen!")
        # Nachname validieren und einlesen
        while True:
            last_name = input("Nachname eingeben: ")
            last_name = last_name.strip()   # leer Zeichen vom Anfang/Ende entfernen
            if not last_name:
                print("Nachname-Feld darf nicht leer sein!")
                continue
            if last_name.replace(" ","").isalpha():
                break
            else:
                print("Eingabe ungültig, erneut versuchen!")

        # Geburtsdatum validieren
        while True:
            date_of_birth = input("Geburtsdatum eingeben TT.MM.JJJJ: ")
            date_of_birth = date_of_birth.strip()
            if not date_of_birth:
                print("Geburtsdatum darf nicht leer sein!")
                continue
            # Format von Geburtsdatum uberprüfen
            if len(date_of_birth) != 10 or date_of_birth[2] != '.' or date_of_birth[5] != '.':
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
            if not address:
                print("Adresse-Feld darf nicht leer sein!")
                continue
            # Variable: es müss mindestens eine Nummer (Hausnummer) vorhanden sein
            has_number = False
            for char in address:
                if char.isdigit():
                    has_number = True
                    break
            # prüfen ob, mindestens eine Zahl und nur Buchstaben/Zahlen und leer Zeichen vorhanden.
            if address.replace(" ", "").isalnum() and has_number:
                break   # Schleife verlassen wenn gültige Adresse
            else:
                # sonst erneut eingeben
                print("Adresse ungültig, erneut versuchen!")

        # Email einlesen und validieren
        while True:
            e_mail = input("Email eingeben: ")
            e_mail = e_mail.strip()  # leer Zeichen vom Anfang/Ende entfernen
            if not e_mail:
                print("Email-Feld darf nicht leer sein!")
                continue
            # Email Länge darf max. 254 stellig sein.
            if len(e_mail) > 254:
                print("Ungültige Email-Adresse, Die Länge darf max. 254 Zeichen sein!")
                continue
            allowed_symbols = ".+-_@"
            for char in e_mail:
                # Überprüfen ob Buchstaben und Zahlen und erlaubte Symbole
                if not (char.isalnum() or char in allowed_symbols):
                    print("Ungültige Email-Adresse, unerlaubte Symbole vorhanden!")
                    break
            # überprüfen ob @ Symbol vorhanden
            if '@' not in e_mail:
                print("Ungültige Email-Adresse, '@' fehlt!")
                continue
            # Mail-Adresse an die Stelle @ teilen, um zu schauen ob nur ein @ vorhanden
            e_mail_parts = e_mail.split('@')
            if len(e_mail_parts) != 2:
                print("Ungültige Email-Adresse, '@' darf nur einmal vorkommen!")
                continue
            # Adresse in username und domain Teile teilen
            before_at, after_at = e_mail_parts
            # überprüfen ob vor '@' und nachher nicht leer ist
            if not before_at or not after_at:
                print("Ungültige Email-Adresse, Username oder Domain fehlt!")
                continue
            #   lokal Teil darf max. 64 Zeichen lang sein
            if len(before_at) > 64:
                print("lokal Teil darf max. 64 Zeichen lang sein")
                continue
            # Überprüfen ob '.' in Domain-Teil vorhanden
            if '.' not in after_at:
                print("Ungültige Email-Adresse, im Domain-Teil fehlt '.'!")
                continue
            # Domain-Teil teilen: an die Stellen wo '.' sind
            after_at_parts = after_at.split('.')
            if len(after_at_parts) > 3:
                print("Ungültige Email-Adresse, im Domain-Teil dürfen max. zwei '.'!")
                continue
            # Die Endung überprüfen: muss min. zweistellig sein ( .at, .com...)
            if len(after_at_parts[-1]) < 2:
                print("Ungültige Email-Adresse, die Endung muss min. zweistellig sein!")
                continue

            # Telefonnummer einlesen und validieren
            while True:
                telefon = input("Telefonnummer eingeben [Format: +43-xxx-xxxxxxx]: ")
                telefon = telefon.strip()
                if not telefon:
                    print("Telefon-Feld darf nicht leer sein!")
                    continue
                # Nummer-Länge überprüfen
                if len(telefon) != 15:
                    print("Telefonnummer ist ungültig!")
                    continue
                # Überprüfen ob nur Zahlen und erlaubte Symbole vorhanden
                for char in telefon:
                    if not (char.isdigit() or char in allowed_symbols):
                        print("Ungültige Nummer, unerlaubte Symbole vorhanden!")
                        break


















    #elif user_choice == 2:

    elif user_choice == 3:
        break

    else:
        print("Ungültige Eingabe! 1, 2 oder 3 eingeben!")
