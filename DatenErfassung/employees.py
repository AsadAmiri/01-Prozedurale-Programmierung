import re
from datetime import date, datetime
# Liste für Personen (Liste von Dictionary)
persons = []


# Funktion: E-Mail validieren
def email_validation(email_address):
    email_address = email_address.strip()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # pattern = r'^(?=.{1,256}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    # Prüfen, ob email_address mit dem regex pattern übereinstimmt
    if re.match(pattern, email_address):
        return True
    else:
        return False

# Funktion: Name validieren
def name_validation(name):
    name = name.replace(" ", "").strip()
    if not name:
        print("Namen-Feld ist leer!")
        return False
    if name.isalpha():
        return True

    print("Ungültige Eingabe, erneut versuchen!")
    return False

# Funktion: Geburtsdatum validieren
def date_of_birth_validation(birthday):
    birthday = birthday.strip()
    try:
        # Umwandelung der eingegebenen Datum im Format: TT.MM.JJJJ
        d_o_birth = datetime.strptime(birthday, "%d.%m.%Y").date()
    except ValueError:
        # Wenn "except ValueError" den Fehler abfängt (falsches Datum/ Format)
        print("Ungültiges Datum oder ungültiges Format [TT.MM.JJJJ]")
        return False

    # Heutiges Datum in today speichern.
    today = date.today()
    if d_o_birth > today:
        print("Geburtsdatum liegt in der Zukunft!")
        return  False
    # Alter ausrechnen
    age = today.year - d_o_birth.year - ((today.month, today.day) < (d_o_birth.month, d_o_birth.day))
    # Wenn Alter kleiner als 18 oder größer als 100 Jahre
    if not (17 < age < 100):
        print("Alter muss zwischen 18 und 100 sein!")
        return False

    return True

# Funktion: Adresse validieren
def address_validation(address):
    address = address.strip()

    pattern = r'^[A-Za-zÄÖÜäöüß\s\.-]+\d+(\s?[A-Za-z0-9/-]*),?\s\d{4}\s+[A-Za-zäöüß]+(?:\s+[A-Za-zäöüß]+)?$'

    if re.match(pattern, address):
        return True
    else:
        return False

# Funktion: Telefonnummer validieren
def telefon_validation(telefon):
    telefon = telefon.strip()

    pattern = r'^\+43[\s/-]?\d[1-9][0-9]{0,3}[\s/-]?\d{3,10}$'
    if re.match(pattern, telefon):
        return True
    else:
        return False

# Funktion: Personendaten bearbeiten oder löschen
def edit_or_delete(persons):
    # Überprüfen, ob überhaupt Personendaten vorhanden sind
    if not persons:
        print("Es sind keine Daten vorhanden.")
        return  # Die Funktion wird beendet, wenn keine Daten vorhanden sind
    # Eingabe: Vorname der Person
    print("Vor- und Nachname der zu bearbeitende Person eingeben")
    firstname = input("Vorname eingeben: ").strip().title()
    # Eingabe: Nachname der Person
    lastname = input("Nachname eingeben: ").strip().title()
    found = False   # Boolean, um festzustellen, ob Person gefunden wurde
    # Durchlaufe alle Personen in Liste, um gesuchte Person zu finden
    for person in persons:
        # Überprüfen ob eingegebene Namen übereinstimmen, wenn so dann ist Person gefunden
        if person['Vorname'] == firstname and  person['Nachname'] == lastname:
            found = True    # Die Person wurde gefunden
            # Ausgabe der gefundenen Person
            print(f"Persondaten gefunden: {person['Vorname']} {person['Nachname']}")
            # Menü Auswahl
            print("Was möchten Sie machen?")
            print("Zum bearbeiten 1 eingeben")
            print("zum löschen 2 eingeben")
            user_action = input("Ihre Eingabe - 1 oder 2: ").strip()

            ## Wenn der User die Option zum Bearbeiten gewählt hat
            if user_action == "1":
                # Liste von Feldern, zum Bearbeiten
                for field in ['Vorname', 'Nachname', 'Geburtsdatum', 'Adresse', 'Email', 'Telefon']:
                    # Aktuellen Wert des Feldes ausgeben
                    print(f"{field} (aktuell): {person[field]}")
                    # Schleife für die neuen Eingaben
                    while True:
                        # Eingabe für das jeweilige Feld
                        new_entry = input(f"Neuen {field} eingeben oder Enter zum behalten: ")
                        new_entry = new_entry.strip()
                        # Wenn keine Eingabe, wird der Bearbeitung für dieses Feld abgebrochen
                        if not new_entry:
                            break
                        # Validierung und Bearbeitung von Vorname oder Nachname
                        if field in ['Vorname', 'Nachname']:
                            # Überprüfe die Gültigkeit des Namens
                            if name_validation(new_entry):
                                # Wenn gültig, wird Name aktualisiert
                                person[field] = new_entry.title()
                                break # Schleife für dieses Feld beenden
                            else:
                                # Fehlermeldung wenn Name ungültig
                                print("Ungültige Eingabe, wird nicht übernommen")
                        # Validierung und Bearbeitung von Geburtsdatum
                        elif field == 'Geburtsdatum':
                            if date_of_birth_validation(new_entry):
                                person[field] = new_entry
                                break
                            else:
                                print("Ungültige Eingabe, wird nicht übernommen")
                        # Validierung und Bearbeitung von Adresse
                        elif field == 'Adresse':
                            if address_validation(new_entry):
                                person[field] = new_entry
                                break
                            else:
                                print("Ungültige Eingabe, wird nicht übernommen")
                        # Validierung und Bearbeitung von E-Mail
                        elif field == 'Email':
                            if email_validation(new_entry):
                                person[field] = new_entry
                                break
                            else:
                                print("Ungültige Eingabe, wird nicht übernommen")
                        # Validierung und Bearbeitung von Telefon
                        elif field == 'Telefon':
                            if telefon_validation(new_entry):
                                person[field] = new_entry
                                break
                            else:
                                print("Ungültige Eingabe, wird nicht übernommen")
                # Bestätigung, dass die Änderungen gespeichert sind
                print("Änderungen wurden gespeichert.\n")
            # Wenn der Benutzer die Option Löschen wählt
            elif user_action == "2":
                # Lösche die Person aus der Liste
                persons.remove(person)
                print("Persondaten wurden gelöscht!")
            # Fehlermeldung bei ungültiger Eingabe
            else:
                print("Ungültige eingabe")
    # Fehlermeldung: wenn keine Person mit dem eingegebenen Vor/Nachnamen gefunden
    if not found:
        print(f"Persondaten mit dem Namen {firstname} {lastname} nicht vorhanden")

# Funktion um gesamte Liste anzuzeigen
def show_whole_list():
    # Durchlaufe jede Person in der Liste "persons"
    for person in persons:
        print("-" * 60)
        # Durchlaufe jedes Feld (key) und sein Wert (value) im Dictionary der aktuellen Person
        for key, value in person.items():
            # Gib den Feldnamen und den Wert aus
            print(f"{key}: {value}")
    print("-" * 60)

# Funktion um gefilterte Liste anzuzeigen
def show_filtered_list():
    # User wird gefragt, nach welchem Feld gefiltert werden soll
    field = input("Wonach wollen Sie filtern? (Vorname, Nachname, Geburtsdatum, Adresse, Email, Telefon, Status): ").strip().title()
    # User gibt den Suchwert ein, nach dem im gewählten Feld gesucht wird
    value = input(f"Nach welchem Wert im Feld '{field}' wollen Sie suchen?: ").strip().title()

    # Liste mit passenden Einträgen erstellen und prüfen ob Feld existiert und gesuchte Wert im Feld vorkommt
    # - Prüft, ob das Feld existiert und ob der gesuchte Wert im Feldinhalt vorkommt
    filtered = [
        person for person in persons
        if field in person and value in person[field].title()
    ]
    # Wenn keine passenden Einträge gefunden sind
    if not filtered:
        print("Keine Einträge gefunden!")
    else:
        # Wenn passende Einträge gefunden
        for person in filtered:
            print("-" * 60)
            # alle Felder der gefundenen Person anzeigen
            for key, value in person.items():
                print(f"{key}: {value}")

    print("-" * 60)


def main():
    while True:
        # Try-except: Fehler abfangen, beim Umwandeln der Eingabe in eine Zahl(int),  wenn keine Zahl eingegeben wird.
        try:
            # Menü anzeigen
            print("** MENÜ **")
            print("1. Persondaten hinzufügen")
            print("2. Persondaten anzeigen")
            print("3. Personendaten bearbeiten")
            print("4. Programm beenden")
            user_choice = int(input("Ihre Eingabe: "))
        except ValueError:
            print("Ungültige Eingabe! Nur 1, 2 oder 3 eingeben!\n")
            continue  # zurück zum Menü

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

            # Name einlesen und mit Hilfe der Funktion validieren
            while True:
                first_name = input("Vorname eingeben: ")
                if not name_validation(first_name):
                    continue

                last_name = input("Nachname eingeben: ")
                if not name_validation(last_name):
                    continue

                break

            # Geburtsdatum einlesen und mit Hilfe der Funktion validieren
            while True:
                date_of_birth = input("Geburtsdatum eingeben [Format TT.MM.JJJJ]: ")
                # Wenn return False ist
                if not date_of_birth_validation(date_of_birth):
                    continue
                break   # wenn gültige Eingabe, dann Schleife beenden

            # Adresse einlesen und mit Hilfe der Funktion validieren
            while True:
                address = input("Adresse eingeben [Format Straße Hausnummer, Posleitzahl(4-stellig) Stadt]: ")
                if address_validation(address):
                    break
                else:
                    print("Ungültige Eingabe, erneut versuchen!")

            # E-Mail-Adresse einlesen und mit Hilfe der Funktion validieren
            while True:
                email = input("Email eingeben: ")
                if email_validation(email):
                    break
                else:
                    print("Ungültige Eingabe, erneut versuchen!")

            # Telefon einlesen und mit Hilfe der Funktion validieren
            while True:
                telefon = input("Telefonnummer eingeben [Format +43 123 123456789]: ")
                if telefon_validation(telefon):
                    break
                else:
                    print("Ungültige Eingabe, erneut versuchen!")

            # die Daten in einem Dictionary speichern.
            person = {
                'Status': person_status,
                'Vorname': first_name.title(),
                'Nachname': last_name.title(),
                'Geburtsdatum': date_of_birth,
                'Adresse': address.title(),
                'Email': email,
                'Telefon': telefon
            }
            # Daten von einzelnen Mitarbeiter in die Liste von personen speichern
            persons.append(person)
            print("\nPersondaten wurden erfolgreich gespeichert!")
            print("_" * 60 + "\n")

        # Personendaten ausgeben, wenn Option 2 ausgewählt ist
        elif user_choice == 2:
            # Wenn die Personenliste leer ist
            if not persons:
                print("Es sind keine Daten vorhanden.")
                continue
            # Menü anzeigen ob Gesamtliste oder Gefilterte anzeigen
            print("1. Gesamtliste anzeigen")
            print("2. Liste filtern")
            user_filter = input("Ihre Eingabe 1 oder 2: ")
            # Gesamtliste anzeigen, mit Funktion
            if user_filter == "1":
                print("\nPersonendaten:")
                show_whole_list()
            # Gefilterte Liste anzeigen
            elif user_filter == "2":
                print("\nPersonendaten:")
                show_filtered_list()

        # Personendaten bearbeiten oder löschen
        elif user_choice == 3:
            edit_or_delete(persons)

        elif user_choice == 4:
            print("Programm wird beendet!")
            break


main()