import streamlit as st
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
c = conn.cursor()

soorten_werk = ["Electra", "Slopen", "Timmerwerk", "Stucwerk", "Schilderwerk", "Betonvloer", "Loodgieter", "Metselwerk", "Isoleren", "Keuken bouwen", "Badkamer bouwen"]
soorten_werk = sorted(soorten_werk)

def create_name_table():
    c.execute('CREATE TABLE IF NOT EXISTS name_table(id INTEGER PRIMARY KEY AUTOINCREMENT, achternaam TEXT,voornaam TEXT, straat TEXT, huisnummer TEXT, postcode TEXT, woonplaats TEXT, telefoonnummer TEXT, email TEXT)')

def create_klus_table():
    c.execute('CREATE TABLE IF NOT EXISTS klus_table(id INTEGER PRIMARY KEY AUTOINCREMENT, klus TEXT, soort_werk TEXT, materiaalkeuze TEXT, prijs REAL, klant_naam TEXT)')

def add_klant(achternaam, voornaam, straat, huisnummer, postcode, woonplaats, telefoonnummer, email):
    c.execute('INSERT INTO name_table(achternaam, voornaam, straat, huisnummer, postcode, woonplaats, telefoonnummer, email) VALUES(?,?,?,?,?,?,?,?)',(achternaam, voornaam, straat, huisnummer, postcode, woonplaats, telefoonnummer, email))
    conn.commit()

    st.success("Gelukt!")

def add_klus(klus, soort_werk, materiaalkeuze, prijs, klant_naam):
    c.execute('INSERT INTO klus_table(klus, soort_werk, materiaalkeuze, prijs, klant_naam) VALUES (?,?,?,?,?)',(klus, soort_werk, materiaalkeuze, prijs, klant_naam))
    conn.commit()
    st.success("Klus toegevoegd: {}".format(klus))

def klanten_overzicht():
    c.execute('SELECT * FROM name_table')
    data = c.fetchall()
    return data

def klussen_overzicht():
    c.execute('SELECT * FROM klus_table')
    data = c.fetchall()
    return data



def nieuwe_klant_form():
    with st.form("Nieuwe klant"):
        achternaam = st.text_input("achternaam")
        voornaam = st.text_input("voornaam")
        straat = st.text_input("straat")
        huisnummer = st.text_input("huisnummer")
        postcode = st.text_input("postcode")
        woonplaats = st.text_input("woonplaats")
        telefoonnummer = st.text_input("telefoonnummer")
        email = st.text_input("email")

        submitted = st.form_submit_button("Toevoegen")
        if submitted:
            add_klant(achternaam, voornaam, straat, huisnummer, postcode, woonplaats, telefoonnummer, email)


def nieuwe_klus_form(klant):

    with st.form("Nieuwe klus", clear_on_submit=True):
        klus = st.text_input("Klus")
        soort_werk = st.selectbox("Soort werk", soorten_werk)
        materiaalkeuze = st.text_input("Materiaal")
        prijs = st.number_input("Begroot in Euro excl. BTW")
        klant_naam = st.text_input("Naam klant", value=klant)



        submitted = st.form_submit_button("Toevoegen")
        if submitted:
            add_klus(klus, soort_werk, materiaalkeuze, prijs, klant_naam)

def unieke_klanten():
    c.execute('SELECT DISTINCT achternaam FROM name_table')
    data = c.fetchall()
    return data

def unieke_klanten_id():
    c.execute('SELECT DISTINCT id FROM name_table')
    data = c.fetchall()
    return data

def klussen_per_klant(achternaam):
    c.execute('SELECT * FROM klus_table WHERE klant_naam = "{}"'.format(achternaam))
    data = c.fetchall()
    return data

