import streamlit as st

st.set_page_config(page_title="Personal Fragebogen", layout="centered")

st.title("📝 Personal Fragebogen")
st.write("Bitte füllen Sie den folgenden Fragebogen sorgfältig aus.")

# --- FORMULAR START ---
with st.form("personal_form"):
    st.header("👤 Persönliche Daten")
    col1, col2 = st.columns(2)
    with col1:
        vorname = st.text_input("Vorname")
        geburtsdatum = st.date_input("Geburtsdatum")
        telefon = st.text_input("Telefonnummer")
    with col2:
        nachname = st.text_input("Nachname")
        geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Divers"])
        email = st.text_input("E-Mail-Adresse")

    st.header("🏠 Adresse")
    strasse = st.text_input("Straße und Hausnummer")
    plz = st.text_input("PLZ")
    ort = st.text_input("Ort")
    land = st.text_input("Land", "Deutschland")

    st.header("🎓 Ausbildung & Beruf")
    schulabschluss = st.selectbox(
        "Höchster Schulabschluss",
        ["Kein Abschluss", "Hauptschule", "Realschule", "Abitur", "Bachelor", "Master", "Promotion"]
    )
    beruf = st.text_input("Aktueller Beruf / Tätigkeit")
    erfahrung = st.slider("Berufserfahrung (Jahre)", 0, 40, 1)

    st.header("💬 Persönliche Einschätzung")
    motivation = st.text_area("Was motiviert Sie beruflich am meisten?")
    staerken = st.text_area("Was sind Ihre größten Stärken?")
    schwächen = st.text_area("Welche Bereiche möchten Sie verbessern?")
    arbeitsstil = st.radio(
        "Wie würden Sie Ihren Arbeitsstil beschreiben?",
        ["Strukturiert", "Kreativ", "Teamorientiert", "Eigenständig", "Flexibel"]
    )

    st.header("📅 Verfügbarkeit")
    startdatum = st.date_input("Frühestes Startdatum")
    arbeitszeit = st.selectbox("Gewünschte Arbeitszeit", ["Vollzeit", "Teilzeit", "Minijob"])

    st.header("🔒 Datenschutz")
    zustimmung = st.checkbox("Ich bestätige, dass meine Angaben korrekt sind und verarbeitet werden dürfen.")

    submitted = st.form_submit_button("Absenden")

# --- FORMULAR ENDE ---

if submitted:
    if not zustimmung:
        st.error("Bitte stimmen Sie der Datenverarbeitung zu.")
    else:
        st.success("Vielen Dank! Ihr Fragebogen wurde erfolgreich übermittelt.")
        st.write("### Ihre Angaben:")
        st.json({
            "Vorname": vorname,
            "Nachname": nachname,
            "Geburtsdatum": str(geburtsdatum),
            "Geschlecht": geschlecht,
            "Telefon": telefon,
            "E-Mail": email,
            "Adresse": f"{strasse}, {plz} {ort}, {land}",
            "Schulabschluss": schulabschluss,
            "Beruf": beruf,
            "Erfahrung": erfahrung,
            "Motivation": motivation,
            "Stärken": staerken,
            "Schwächen": schwächen,
            "Arbeitsstil": arbeitsstil,
            "Startdatum": str(startdatum),
            "Arbeitszeit": arbeitszeit
        })
