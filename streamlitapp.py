
import streamlit as st

st.set_page_config(page_title="Einfaches Formular", page_icon="📝")

st.title("Einfaches Eingabeformular")

# Formular
with st.form("eingabe_formular"):
    name = st.text_input("Name eingeben:")
    alter = st.number_input("Alter eingeben:", min_value=0, max_value=120, step=1)
    bemerkung = st.text_area("Bemerkung:")

    submit = st.form_submit_button("Absenden")

# Ausgabe nach Button-Klick
if submit:
    st.success("Eingegebene Werte:")

    st.write(f"**Name:** {name}")
    st.write(f"**Alter:** {alter}")
    st.write(f"**Bemerkung:** {bemerkung if bemerkung else '-'}")




