import json # zum json datei zu bearbeiten
import os   # zum überprüfen ob eine Datei existiert oder nicht
import re   # regex um zu validieren
from tkinter import *
from tkinter import messagebox  # GUI Info/Fehler zeigen
from tkinter import ttk  # Für dropdown (Combobox)
from datetime import datetime   # um mit Datum zu arbeiten

# Funktion: Datei "persons.json" in Lesemodus öffnen, wenn nicht existiert dann leere Liste zurückgeben
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file) # eine Pythonliste zurückgeben
    else:
        return []

# Funktion: Daten in json Format speichern
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=1) # Pythonliste(data) in json speichern

# Name validieren
def validate_name(name):
    pattern = r"[A-ZÄÖÜ][a-zäöüß]+(-[A-ZÄÖÜ][a-zäöüß]+)?(\s[A-ZÄÖÜ][a-zäöüß]+(-[A-ZÄÖÜ][a-zäöüß]+)?)+"
    if re.fullmatch(pattern, name):
        return True
    else:
        return False

# Telefon validieren
def validate_telefon(telefon):
    pattern =r"\+43\s?\d{5,12}"
    if re.fullmatch(pattern, telefon):
        return True
    else:
        return False

# E-Mail validieren
def validate_email(email):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

# Geburtstag validieren
def validate_date_of_birth(date):
    try:
        date = datetime.strptime(date, "%d.%m.%Y")
        return date <= datetime.now()
    except ValueError:
        return False

# Adresse validieren
def validate_address(address):
    pattern = r"[A-Za-zÄÖÜäöüß\s\.-]+\d+(\s?[A-Za-z0-9/-]*),\s\d{4}\s[A-Za-zäöüß]+(?:\s[A-Za-zäöüß]+)?"
    if re.fullmatch(pattern, address):
        return True
    else:
        return False

# Alter ausrechnen
def calculate_age(birthday):
    # versuchen Str-Geburtsdatum in Datum umwandeln
    try:
        birthdate = datetime.strptime(birthday, "%d.%m.%Y")
        today = datetime.today()
        # Alter berechnen
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    except:
        # Wenn Datum ungültig ist, gib None zurück
        return None


# Funktion: um Daten zu zeigen
def show_data_gui(filter_mode=False, filter_type="All", filter_value=""):
    persons = load_data("persons.json")  # Daten von persons.json laden
    text_area.delete(1.0, END)  # text_area für die Anzeige löschen
    # Wenn keine Daten vorhanden sind
    if not persons:
        text_area.insert(END, "Keine Daten vorhanden.\n")
        return
    # Eine Liste für gefilterte Personen
    filtered_persons = []
    # Wenn Filtermodus aktiviert ist
    if filter_mode:
        # Schleife über alle Personen und ihre Daten laufen lassen und ein String erstellen
        for person in persons:
            person_data = f"{person['name']} {person['date_of_birth']}{person['telefon']} {person['email']} {person['address'] } {person['person_type']}".lower()
            # Wenn der Filtertyp "Alle" ist oder der Filterwert im Personen-Datenstring enthalten ist
            if filter_type == "Alle" or filter_value.lower() in person_data:
                filtered_persons.append(person)
    else:
        filtered_persons = persons  # Kein Filter, Alle Personen anzeigen

    # Wenn keine übereinstimmende Daten gefunden
    if not filtered_persons:
        text_area.insert(END, "Keine Daten gefunden.\n")
        return

    # für jede gefilterte Person Daten zeigen
    for person in filtered_persons:
        # Ausgabe der Personendaten
        person_data = f"ID: {person['id']}\n" \
                      f"Name: {person['name']}\n" \
                      f"Geburtsdatum: {person['date_of_birth']}\n" \
                      f"Telefonnummer: {person['telefon']}\n" \
                      f"E-Mail: {person['email']}\n" \
                      f"Adresse: {person['address']}\n" \
                      f"Person ist: {person['person_type']}\n"

        # Überprüfen ob Geburtsmonat/Geburtstag ist
        try:
            # Geburtsdatum in Datetime Obj konvertieren
            birth_date = datetime.strptime(person["date_of_birth"], "%d.%m.%Y")
            today = datetime.today()
            # wenn Geburtsmonat ist gleich wie aktueller Monat
            if birth_date.month == today.month:
                # Geburtstagsdatum für aktuelle Jahr erstellen
                this_year_birthday = birth_date.replace(year=today.year)
                text_area.insert(END, "Geburtsmonat 🎂\n")
                # wenn Geburtstag heute ist
                if this_year_birthday.date() == today.date():
                    text_area.insert(END, "Alles gute zum Geburtstag 🎂\n")
                else:   # Unterschied der Tagen berechnen (zum nächsten Geburtstag)
                    days_difference = (this_year_birthday - today).days
                    # wenn der Geburtstag noch nicht gekommen
                    if days_difference > 0:
                        text_area.insert(END, f"Noch {days_difference} Tage bis zum Geburtstag\n")
                    else:   # wenn Geburtstag schon vorbei ist
                        text_area.insert(END, f"Geburtstag war vor {-days_difference} Tagen\n")
        except:
            pass

        # String Personendaten in text_area anzeigen und eine Trennlinie
        text_area.insert(END, person_data)
        text_area.insert(END, "\n" + '-' * 40 + "\n")


# Funktion um Filter zurücksetzen
def reset_filter():
    filter_option.set("Alle")
    filter_input_entry.delete(0, END)

# Funktion: um eine neue Person hinzufügen
def add_person_gui():
    # Nimmt Daten von "Entry Fields" und erstellt ein Dict. person
    person = {
        "id": id_entry.get().strip(),
        "name": name_entry.get().strip(),
        "date_of_birth": date_of_birth_entry.get().strip(),
        "telefon": telefon_entry.get().strip(),
        "email": email_entry.get().strip(),
        "address": address_entry.get().strip(),
        "person_type": mitarbeiter_besucher_option.get()
    }
    # ID Feld überprüfen ob leer ist
    if not person["id"]:
        messagebox.showerror("Fehler", "ID darf nicht leer sein.")
        return  # Funktion beenden
    # Überprüfung des Namens mit der Funktion validate_name
    if not validate_name(person["name"]):
        messagebox.showerror("Fehler", "Ungültiger Name.") # Wenn ungültig Fehler anzeigen
        return  # Funktion beenden, keine Person speichern
    # Überprüfung des Geburtsdatums mit der Funktion validate_date_of_birth
    if not validate_date_of_birth(person["date_of_birth"]):
        messagebox.showerror("Fehler", "Ungültiges Geburtsdatum.")
        return  # Funktion beenden
    # Überprüfung der Telefonnummer mit der Funktion validate_telefon
    if not validate_telefon(person["telefon"]):
        messagebox.showerror("Fehler", "Ungültige Telefonnummer.")
        return
    # Überprüfung der E-Mail mit der Funktion validate_email
    if not validate_email(person["email"]):
        messagebox.showerror("Fehler", "Ungültige E-Mail.")
        return
    # Überprüfung der Adresse mit der Funktion validate_address
    if not validate_address(person["address"]):
        messagebox.showerror("Fehler", "Ungültige Adresse.")
        return

    # Daten aus Datei "persons.json" laden
    persons = load_data("persons.json")

    # Überprüfen ob ID schon existiert
    for existing_person in persons:
        if existing_person["id"] == person["id"]:
            messagebox.showerror("Fehler", "ID ist schon vergeben!")
            return

    # Persondaten in Liste speichern
    persons.append(person)
    save_data("persons.json", persons)  # Liste in json Datei speichern
    # eine Erfolgsmeldung anzeigen
    messagebox.showinfo("Erfolg", "Person erfolgreich gespeichert!")
    # Alle Entry-Fields zurücksetzen
    for entry in [id_entry, name_entry, date_of_birth_entry, telefon_entry, email_entry, address_entry]:
        entry.delete(0, END)
    # In text_area anzeigen, dass name+id gespeichert
    text_area.insert(END, f"{person['name']} ({person['id']}) gespeichert\n")

# Funktion: um Daten zu ändern/bearbeiten
def edit_person_gui():
    # Daten von json Datei laden
    persons = load_data("persons.json")
    # ID von User aus id_entry holen, um zu bearbeiten
    person_id = id_entry.get().strip()
    # überprüfen ob ID leer ist
    if not person_id:
        messagebox.showerror("Fehler", "Bitte ID eingeben!")
        return
    # Person mit eingegebener ID suchen
    found = False # um zu Überprüfen ob sie Person gefunden wurde
    for person in persons:  # Schleife durch alle Personen
        # Wenn eine Person mit der gleichen ID gefunden wird, Person in person_to_edit
        if person["id"] == person_id:
            person_to_edit = person
            found = True
            break
    # Fehlermeldung wenn Person nicht gefunden wurde
    if not found:
        messagebox.showerror("Fehler", "Person mit dieser ID wurde nicht gefunden!")
        return

    # Wenn die Person gefunden, aktuelle Daten in Entry-Fields anzeigen
    name_entry.delete(0, END)   # Vorherige Werte löschen, wenn vorhanden
    name_entry.insert(0, person_to_edit["name"]) # Neuen Name einfügen

    date_of_birth_entry.delete(0, END)
    date_of_birth_entry.insert(0, person_to_edit["date_of_birth"])

    telefon_entry.delete(0, END)
    telefon_entry.insert(0, person_to_edit["telefon"])

    email_entry.delete(0, END)
    email_entry.insert(0, person_to_edit["email"])

    address_entry.delete(0, END)
    address_entry.insert(0, person_to_edit["address"])

# Funktion: Nach der Bearbeitung, validieren und speichern
def save_changes():
    person_id = id_entry.get().strip() # ID der Person holen, die bearbeitet wird
    persons = load_data("persons.json") # Daten aus json Datei holen
    # found, ob die Person gefunden wurde
    found = False
    for person in persons: # ID suchen und die Person, in person_to_edit speichern
        if person["id"] == person_id:
            person_to_edit = person
            found = True
            break
    # wenn Person nicht gefunden, found bleibt False
    if not found:
        messagebox.showerror("Fehler", "Person mit dieser ID wurde nicht gefunden!")
        return

    # die neue Daten von Entry-Fields holen
    updated_person = {
        "id": person_to_edit["id"],  # ID muss gleich bleiben
        "name": name_entry.get().strip(),
        "date_of_birth": date_of_birth_entry.get().strip(),
        "telefon": telefon_entry.get().strip(),
        "email": email_entry.get().strip(),
        "address": address_entry.get().strip(),
        "person_type": mitarbeiter_besucher_option.get()
    }
    # die neuen Daten validieren
    if not validate_name(updated_person["name"]):
        messagebox.showerror("Fehler", "Ungültiger Name!")
        return
    if not validate_date_of_birth(updated_person["date_of_birth"]):
        messagebox.showerror("Fehler", "Ungültiges Geburtsdatum!")
        return
    if not validate_telefon(updated_person["telefon"]):
        messagebox.showerror("Fehler", "Ungültige Telefonnummer!")
        return
    if not validate_email(updated_person["email"]):
        messagebox.showerror("Fehler", "Ungültige E-Mail!")
        return
    if not validate_address(updated_person["address"]):
        messagebox.showerror("Fehler", "Ungültige Adresse!")
        return
    # neue Persondaten in der Liste aktualisieren
    for i, person in enumerate(persons):
        if person["id"] == person_id:
            persons[i] = updated_person
            break
    # neue Daten in json speichern, von aktualisierte Liste persons
    save_data("persons.json", persons)
    # Erfolgsmeldung anzeigen und Entry-Fields löschen
    messagebox.showinfo("Erfolg", "Daten erfolgreich geändert!")
    clear_fields()  # Eingabefelder zurücksetzen

# Funktion: alle Entry-Fields löschen, nach erfolgreicher Speicherung
def clear_fields():
    for entry in [id_entry, name_entry, date_of_birth_entry, telefon_entry, email_entry, address_entry]:
        entry.delete(0, END)

# Funktion: um Text Area zu löschen
def delete_text_area():
    text_area.delete("1.0", END)

############################### GUI TEIL ###############################################

# das Hauptfenster erstellen, root ist ein Objekt der Tk()-Klasse
root = Tk()
# Fenstertitel
root.title("Daten Management System")
# Setze die Fenstergröße
root.geometry("1115x700")
# Setze die Hintergrundfarbe des Fensters
root.configure(bg="#8B7D7B")
# # Füge ein Fenster-Icon hinzu
#root.iconbitmap("title_icon.ico")
# Hier erstellen wir ein Überschriften-Label (Daten Management System)
heading_label = Label(root, text="Daten Management System", font=("Helvetica", 24, "bold"), background="#8B7D7B",
                      foreground="midnightblue", border=10)
# Positioniere das Label im Fenster – pack() setzt es oben zentriert, fill=X (horizental ausgehnen)
heading_label.pack(fill=X)
# Erstelle ein LabelFrame für Details wie Name, Telefon usw. "Persondaten" ist der Titel dieses Rahmens
person_details_frame = LabelFrame(root, text="Persondaten", font=("Helvetica", 18, "bold"), foreground="midnightblue",
                                  border=6, background="#8B7D7B")
person_details_frame.pack(fill=X)
# Name-Label im Rahmen hinzufügen
name_label = Label(person_details_frame, text="Name", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
# Positioniere das Name-Label mit grid() – gibt Zeile und Spalte an
name_label.grid(row=0, column=0)
# Eingabefeld für den Namen
name_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
name_entry.grid(row=0, column=1)   # positioniere es mit grid()
# Label für Geburtsdatum
date_of_birth_label = Label(person_details_frame, text="Geburtsdatum", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
date_of_birth_label.grid(row=0, column=2)  # positioniere es mit grid()
# Eingabefeld für Geburtsdatum
date_of_birth_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
date_of_birth_entry.grid(row=0, column=3)
# Label für ID
id_label = Label(person_details_frame, text="ID", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
id_label.grid(row=1, column=0)
# Eingabefeld für ID
id_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
id_entry.grid(row=1, column=1)
# Label für Adresse
address_label = Label(person_details_frame, text="Adresse", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
address_label.grid(row=0, column=4)
# Eingabefeld für Adresse
address_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
address_entry.grid(row=0, column=5)
# Label für E-Mail
email_label = Label(person_details_frame, text="E-Mail", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
email_label.grid(row=1, column=2)
# Eingabefeld für E-Mail
email_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
email_entry.grid(row=1, column=3)
# Label für Telefonnummer
telefon_label = Label(person_details_frame, text="Telefonnummer", bg="#8B7D7B", font=("Helvetica", 14, "bold"), fg="black")
telefon_label.grid(row=1, column=4)
# Eingabefeld für Telefonnummer
telefon_entry = Entry(person_details_frame, font=("Helvetica", 14), border=3)
telefon_entry.grid(row=1, column=5)
# Label für Mitarbeiter oder Besucher
mitarbeiter_besucher_label = Label(person_details_frame, text="Person ist:", font=("Helvetica", 14, "bold"), bg="#8B7D7B")
mitarbeiter_besucher_label.grid(row=2, column=0)
# Dropdown Menü für Auswahl zwi. Mitarbeiter/ Besucher
mitarbeiter_besucher_option = ttk.Combobox(person_details_frame, font=("Helvetica", 14), values=["Mitarbeiter/in", "Besucher/in"], width=19)
mitarbeiter_besucher_option.grid(row=2, column=1, pady=5)
mitarbeiter_besucher_option.current(0)
# Rahmen für die Ausgabefläche
output_frame = Frame(root)
output_frame.pack()
# Überschrift für Ausgabebereich (Personendaten: )
output_frame_label = Label(output_frame, text="Personendaten", font=("Helvetica", 20, "bold"), bg="#8B7D7B")
output_frame_label.pack(fill=X)
# Scrollbar hinzufügen
text_area_scrollbar = Scrollbar(output_frame, orient=VERTICAL)
text_area_scrollbar.pack(side=RIGHT, fill=Y)
# Textfeld zur Anzeige der Daten und mit scrollbar verbinden
text_area = Text(output_frame, height=20, width=80, yscrollcommand=text_area_scrollbar.set)
text_area.pack()
# Scrollbar konfigurieren, damit sie funktioniert
text_area_scrollbar.config(command=text_area.yview)
# Rahmen für die Buttons (Hinzufügen, ID Suchen, Löschen usw.)
buttons_frame = Frame(root, pady=10, bg="#8B7D7B", bd=5)
buttons_frame.pack(anchor="center") # Button-Rahmen platzieren
# Button: Daten hinzufügen
add_button = Button(buttons_frame, text="Daten Hinzufügen", font=("Helvetica", 14, "bold"), border=3, width=15, command=add_person_gui)
add_button.grid(row=0, column=0, padx=10)
# Button: ID suchen
edit_button = Button(buttons_frame, text="ID Suchen", font=("Helvetica", 14, "bold"), border=3, width=15, command=edit_person_gui)
edit_button.grid(row=0, column=1, padx=10)
# Button: Löschen
delete_button = Button(buttons_frame, text="Löschen", font=("Helvetica", 14, "bold"), border=3, width=15, command=delete_text_area)
delete_button.grid(row=0, column=3, padx=10)
# Button: Änderungen speichern
save_changes_button = Button(buttons_frame, text="Änderung speichern", font=("Helvetica", 14, "bold"), border=3, width=17, command=save_changes)
save_changes_button.grid(row=0, column=4, padx=10)
# Filterbereich
filter_frame = Frame(root, bg="#8B7D7B", pady=10)
filter_frame.pack(fill=X)
# Label für Filterbereich
filter_label = Label(filter_frame, text="Filtern nach:", font=("Helvetica", 14, "bold"), bg="#8B7D7B")
filter_label.grid(row=0, column=0, padx=10)
# Dropdown um Filtertyp zu wählen (z.B. filtern nach: Name, Email usw.)
filter_option = ttk.Combobox(filter_frame, font=("Helvetica", 14), values=["Alle", "Name", "Geburtsdatum", "Telefonnummer", "E-Mail", "Adresse"])
filter_option.current(0)  # Standard = "Alle"
filter_option.grid(row=0, column=1, padx=10)
# Eingabefeld für Filterwert
filter_input_entry = Entry(filter_frame, font=("Helvetica", 14), border=3)
filter_input_entry.grid(row=0, column=2, padx=10)
# Button: Filter anwenden
filter_button = Button(filter_frame, text="Daten Zeigen", font=("Helvetica", 14, "bold"), border=3, width=17,
                       command=lambda: show_data_gui(filter_mode=True, filter_type=filter_option.get(), filter_value=filter_input_entry.get()))
filter_button.grid(row=0, column=3, padx=10)
# Filter Button zurücksetzen
reset_filter_button = Button(filter_frame, text="Filter Zurücksetzen", font=("Helvetica", 14, "bold"), border=3, width=15, command=reset_filter)
reset_filter_button.grid(row=0, column=4, padx=10)
# Haupt-Loop: Hält das Fenster offen, bis der Benutzer es schließt
root.mainloop()
