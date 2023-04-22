import streamlit as st
import pandas as pd
from db_fxns import *
from word_fxns import *
from aggrid_test import *

st.set_page_config(page_title="Tabellen", page_icon=":hammer:", layout="wide")
create_name_table()
create_klus_table()
menu = ["Klantenoverzicht", "Nieuwe klus", "Nieuwe klant", "Klussenoverzicht", "Rekeningen"]
klanten = sorted([i[0] for i in unieke_klanten()])
choice = st.sidebar.selectbox("Menu", menu)

kolommen_klant = ['id','achternaam', 'voornaam', 'straat', 'huisnummer', 'postcode', 'woonplaats', 'telefoonnummer', 'email']
kolommen_klus = ['id','klus', 'soort werk', 'materiaalkeuze', 'prijs', 'klant naam']

if choice == 'Klantenoverzicht':

    st.subheader("Klantenoverzicht")
    result = klanten_overzicht()
    df = pd.DataFrame(result, columns=kolommen_klant)
    st.dataframe(df)
    #st.write(unieke_klanten_id())
    st.subheader("Klussen per klant")
    klanten_keus = st.selectbox("Kies klant", klanten)
    result_2 = klussen_per_klant(klanten_keus)
    df_2 = pd.DataFrame(result_2, columns=kolommen_klus)
    st.dataframe(df_2)

elif choice == 'Nieuwe klant':
    st.subheader("Nieuwe klant")
    nieuwe_klant_form()

elif choice == 'Nieuwe klus':
    st.write("Selecteer de klant waar je een klus voor wil doen: ")
    lijst_met_klanten = [i[0] for i in unieke_klanten()]
    #lijst_met_klanten_ids = [i[0] for i in unieke_klanten_id()]
    klant = st.selectbox("Klant", sorted(lijst_met_klanten))
    st.write(klant)

    nieuwe_klus_form(klant)

elif choice == 'Klussenoverzicht':
    st.subheader("Klussenoverzicht")
    result = klussen_overzicht()
    df = pd.DataFrame(result, columns=kolommen_klus)
    st.dataframe(df)

elif choice == "Rekeningen":
    st.subheader("Rekeningen")
    st.markdown("""---""")
    klanten_keus = st.selectbox("Kies klant", klanten)
    result_2 = klussen_per_klant(klanten_keus)
    df_2 = pd.DataFrame(result_2, columns=kolommen_klus)
    #st.dataframe(df_2)
    st.markdown("""---""")
    selectie = selecteer_klussen(df_2)

    if st.button("Maak rekening"):
        bill(klanten_keus, selectie)
        st.success("Rekening gemaakt")











# (achternaam, voornaam, straat, huisnummer, postcode, woonplaats, telefoonnummer, email)