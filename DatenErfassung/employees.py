# Leere Liste um Personendaten zu speichern
persons = []

# Endlose Schleife um Menü wiederholt zu zeigen
while True:

    # Try-except: Fehler abfangen, beim Umwandeln der Eingabe in eine Zahl(int),  wenn keine Zahl eingegeben wird.
    try:
        # Menü anzeigen
        print("** MENÜ **")
        print("1. Persondaten hinzufügen")
        print("2. Persondaten anzeigen")
        print("3. Progream beenden")
        user_choice = int(input("Ihre Eingabe: "))
    except ValueError:
        print("Ungültige Eingabe! Nur 1, 2 oder 3 eingeben!\n")
        continue    # zurück zum Menü

    if user_choice == 1:

        # Besucher*in oder Mitarbeiter*in
        while True:
            person_status = ""
            print("\nEin*e Mitarbeiter*in oder ein*e Besucher*in erfassen?")
            print("1. für Mitarbeiter*in")
            print("2. für Besucher*in")
            try:
                arbeiter_besucher = int(input("Ihre Eingabe (1 oder 2): "))
            except ValueError:
                print("Ungültige Eingabe! Nur 1 oder 2 eingeben!")
                continue

            if arbeiter_besucher == 1:
                person_status = "Mitarbeiter*in"
                break
            elif arbeiter_besucher == 2:
                person_status = "Besucher*in"
                break
            else:
                print("Ungültige Eingabe! Nur 1 oder 2 eingeben!")
                continue

        # Vorname validieren und einlesen
        while True:
            first_name = input("\nVorname eingeben: ")
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
            # mit try-except fehler abfangen, falls keine Zahleneingabe
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
                print("Jahr darf zwischen 1925 und 2008 sein!")
                continue # wenn jünger als 18 oder älter als 100, erneute Eingabe auffordern
            # Monat validieren
            if month < 1 or month > 12:
                print("Monat muss zwischen 1 und 12 sein!")
                continue

            # Anzahl der Tagen in einem Monat festlegen
            months_with_30 = [4, 6, 9, 11] # April, Juni, September, November
            if month == 2:
                # Falls Schaltjahr: Feb. = 29
                if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_days = 29
                else:
                    max_days = 28
            elif month in months_with_30: # April, Juni, September, November
                max_days = 30
            else:
                max_days = 31   # Jan. Mär. Mai. Jul. Aug. Okt. Dez.
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

            allowed_symbols = ",.-/ "
            # Variablen: es mussen Alphabeten Nummer (Hausnummer) oder auch erlaubte Zeichen vorhanden sein
            has_digit = False
            has_alpha = False
            valid_symbols = True

            for char in address:
                # Überprüfung für Digit (z.B. Hausnummer)
                if char.isdigit():
                    has_digit = True
                # Überprüfung für Alphabeten
                elif char.isalpha():
                    has_alpha = True
                # Überprüfung ob erlaubte Symbole vorhanden
                elif not (char in allowed_symbols):
                    valid_symbols = False
                    break
            # Überprufen ob Alphabet, Zahl und nur erlaubte Symbole vorhanden sind
            if has_alpha and has_digit and valid_symbols:
                break   # Falls gültige Eingabe, while-schleife beenden
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
            # Variable für erlaubte Symbole initializieren
            allowed_symbols = ".+-_@"
            # Boolean Variable: annehmen dass nur erlaubte Symbole vorhanden
            symbols = True
            for char in e_mail:
                # Überprüfen ob Buchstaben und Zahlen und erlaubte Symbole
                if not (char.isalnum() or char in allowed_symbols):
                    print("Ungültige Email-Adresse, unerlaubte Symbole vorhanden!")
                    # Variable auf False setzen, wenn unerlaubte Symbole vorhanden
                    symbols = False
                    # For-Schleife beenden
                    break
            # Falls unerlaubte Symbole vorhanden, erneut auffordern.
            if not symbols:
                continue
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

            # break wenn alles gültig
            break

        # Telefonnummer einlesen und validieren
        while True:
            telefon = input("Telefonnummer eingeben [Format: +xx-xxx-xxxxxxx]: ")
            telefon = telefon.strip()   # leer Zeichen von Anfang und Ende entfernen
            # Falls Telefonfeld leer ist
            if not telefon:
                print("Telefon-Feld darf nicht leer sein!")
                continue
            # Nummer-Länge überprüfen
            if len(telefon) != 15:
                print("Telefonnummer ist ungültig!")
                continue
            # mit '+' beginnen und Länderwahl, Anbieter und Nummer mit '-' trennen
            if telefon[0] != '+' or telefon[3] != '-' or telefon[7] != '-':
                print("Ungültige Format Eingabe! [Format: +xx-xxx-xxxxxxx]")
                continue
            # Überprüfen ob nur Zahlen als Nummer eingegeben sind.
            if not (telefon[1:3].isdigit() and telefon[4:7].isdigit() and telefon[8:].isdigit()):
                print("Telefonnummer ist ungültig! nur Zahlen eingeben!")
                continue

            # break wenn alles gültig
            break

        # die Daten in einem Dictionary speichern.
        person = {
            'Status': person_status,
            'Vorname': first_name.title(),
            'Nachname': last_name.title(),
            'Geburtsdatum': date_of_birth,
            'Adresse': address.title(),
            'Email': e_mail,
            'Telefon': telefon
            }
        # Daten von einzelnen Mitarbeiter in die Liste von personen speichern
        persons.append(person)
        print("\nPersondaten wurden erfolgreich gespeichert!")
        print("_" * 60 + "\n")

    # Option 2 für die Ausgabe
    elif user_choice == 2:
        # Falls die Liste leer ist
        if not persons:
            print("\nDie Liste ist leer!\n")
            continue    # erneut auffordern

        while True:
            try:
                print("\n1. Mitarbeiterliste anzeigen\n2. Besucherliste anzeigen\n3. Beide anzeigen")
                output_choice = int(input("Ihre Eingabe: "))
            except ValueError:
                print("Ungültige Eingabe, 1, 2 oder 3 eingeben!")
                continue

            print("-" * 60)
            print(f"\n** Liste der gespeicherten Personen **")
            print("-" * 60)

            # Eingabe: 1, wird nur die Liste von Mitarbeiter*in gezeigt
            if output_choice == 1:
                # Die Liste von persons durchlaufen und auch Index ausgeben
                for index, person in enumerate(persons, start=1):
                    if person["Status"] == "Mitarbeiter*in":
                        # Alle Ausgaben: Index, Name, Geburtsdatum...
                        print(f"Person: {index}")
                        print(f"Status: {person['Status']}")
                        print(f"Name: {person['Vorname']} {person['Nachname']}")
                        print(f"Geburtsdatum: {person['Geburtsdatum']}")
                        print(f"Adresse: {person['Adresse']}")
                        print(f"Email: {person['Email']}")
                        print(f"Telefon: {person['Telefon']}")
                        print("-" * 60 + "\n")
                break   # nach Ausgabe, innere Schleife beenden und zurück zur Haupt-Menü

            # Eingabe: 2, wird nur die Liste von Besucher*in gezeigt
            elif output_choice == 2:
                # Die Liste von persons durchlaufen und auch Index ausgeben
                for index, person in enumerate(persons, start=1):
                    if person["Status"] == "Besucher*in":
                        # Alle Ausgaben: Index, Name, Geburtsdatum...
                        print(f"Person: {index}")
                        print(f"Status: {person['Status']}")
                        print(f"Name: {person['Vorname']} {person['Nachname']}")
                        print(f"Geburtsdatum: {person['Geburtsdatum']}")
                        print(f"Adresse: {person['Adresse']}")
                        print(f"Email: {person['Email']}")
                        print(f"Telefon: {person['Telefon']}")
                        print("-" * 60 + "\n")
                break   # nach Ausgabe, innere Schleife beenden und zurück zur Haupt-Menü

            # Eingabe: 3, gesamte Liste wird angezeigt (Mitarbeiter*in und Besucher*in)
            elif output_choice == 3:
                # Die Liste von persons durchlaufen und auch Index ausgeben
                for index, person in enumerate(persons, start=1):
                    print(f"Person: {index}")
                    print(f"Status: {person['Status']}")
                    print(f"Name: {person['Vorname']} {person['Nachname']}")
                    print(f"Geburtsdatum: {person['Geburtsdatum']}")
                    print(f"Adresse: {person['Adresse']}")
                    print(f"Email: {person['Email']}")
                    print(f"Telefon: {person['Telefon']}")
                    print("-" * 60 + "\n")
                break   # nach Ausgabe, innere Schleife beenden und zurück zur Haupt-Menü
            else:
                print("Ungültige Eingabe, 1, 2 oder 3 eingeben!")


    # Option 3 um Programm mit break zu beenden
    elif user_choice == 3:
        print("Programm wird beendet!")
        break
    # Wenn Zahlen ausser 1, 2 oder 3 eingegeben wird
    else:
        print("\nUngültige Eingabe! 1, 2 oder 3 eingeben!\n")




