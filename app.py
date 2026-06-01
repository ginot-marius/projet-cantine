import streamlit as st

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Suivi Cantine - EPLE", page_icon="🥗", layout="centered")

# 2. PERSONNALISATION VISUELLE (CSS)
# On injecte du code pour mettre l'image de fond et styliser les blocs
st.markdown("""
    <style>
    /* Image de fond */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1574966739982-2b7849ec631c?q=80&w=1920");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Bloc principal semi-transparent pour la lisibilité */
    .main-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    /* Style des titres */
    h1 {
        color: #2E7D32 !important;
        text-shadow: 1px 1px 2px white;
        text-align: center;
    }
    
    h2, h3 {
        color: #1B5E20 !important;
    }

    /* Style pour le tableau pour qu'il ressorte */
    .stTable {
        background-color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENU DE L'APPLICATION
st.title("🥗 Grand Suivi des Déchets - CDSG")
st.markdown('<div class="main-box">Cette application permet de visualiser l\'impact écologique de nos établissements du projet <b>EPLE bas carbone</b>.</div>', unsafe_allow_html=True)

# Données des établissements
donnees_etablissements = {
    "COLLEGE J. GIONO": {"plastique": 12.4, "serviettes": 4.2, "alimentaire": 35.8, "fruits": 8.5, "pain": 14.0},
    "LYCEE DE L'ARC": {"plastique": 22.1, "serviettes": 9.5, "alimentaire": 64.0, "fruits": 15.2, "pain": 28.3},
    "COLLEGE ARAUSIO": {"plastique": 10.5, "serviettes": 3.8, "alimentaire": 29.4, "fruits": 7.1, "pain": 11.2},
    "LP ARGENSOL": {"plastique": 15.2, "serviettes": 5.0, "alimentaire": 42.1, "fruits": 9.0, "pain": 19.5},
    "COLLEGE B. HENDRICKS": {"plastique": 11.0, "serviettes": 4.0, "alimentaire": 31.5, "fruits": 8.0, "pain": 13.4},
    "LP A. BRIAND": {"plastique": 14.8, "serviettes": 6.2, "alimentaire": 45.0, "fruits": 11.3, "pain": 21.0},
    "LYCEE VITICOLE": {"plastique": 8.5, "serviettes": 2.9, "alimentaire": 24.7, "fruits": 5.4, "pain": 10.1},
    "ENSEMBLE SCOLAIRE SAINT LOUIS": {"plastique": 13.0, "serviettes": 4.8, "alimentaire": 38.2, "fruits": 9.1, "pain": 16.5},
    "LYCEE L. AUBRAC": {"plastique": 19.5, "serviettes": 8.0, "alimentaire": 58.4, "fruits": 14.0, "pain": 25.2},
    "COLLEGE H. BOUDON": {"plastique": 9.4, "serviettes": 3.1, "alimentaire": 27.0, "fruits": 6.5, "pain": 10.5},
    "COLLEGE P. ELUARD": {"plastique": 11.8, "serviettes": 4.5, "alimentaire": 33.1, "fruits": 8.2, "pain": 14.8},
    "COLLEGE VALLIS AERIA": {"plastique": 10.2, "serviettes": 3.6, "alimentaire": 28.9, "fruits": 7.0, "pain": 12.0},
    "LP F. REVOUL": {"plastique": 12.0, "serviettes": 4.1, "alimentaire": 36.0, "fruits": 8.7, "pain": 15.2},
    "ES SAINT-JEAN-LE -BAPTISTE": {"plastique": 11.5, "serviettes": 4.3, "alimentaire": 34.2, "fruits": 8.0, "pain": 13.9},
    "COLLEGE V. SCHOELCHER": {"plastique": 12.9, "serviettes": 5.1, "alimentaire": 40.5, "fruits": 9.8, "pain": 17.1},
    "COLLEGE SAINT-EXUPERY": {"plastique": 14.1, "serviettes": 5.8, "alimentaire": 44.2, "fruits": 10.5, "pain": 19.0},
    "école Jules Ferry": {"plastique": 6.2, "serviettes": 2.1, "alimentaire": 18.0, "fruits": 4.5, "pain": 7.3},
    "école du grillon": {"plastique": 5.8, "serviettes": 1.9, "alimentaire": 16.5, "fruits": 4.0, "pain": 6.8},
    "école curie": {"plastique": 7.5, "serviettes": 2.8, "alimentaire": 21.3, "fruits": 5.1, "pain": 8.9}
}

# Sélection de l'établissement
with st.container():
    st.header("🏫 Établissement")
    liste = list(donnees_etablissements.keys())
    choix = st.selectbox("Choisir dans la liste :", liste)

infos = donnees_etablissements[choix]
total = infos["plastique"] + infos["serviettes"] + infos["alimentaire"] + infos["fruits"] + infos["pain"]

# Tableau de bord
st.markdown("---")
st.header(f"📋 Résultats pour {choix}")

tableau = {
    "Poubelles de Tri": [
        "Emballages plastiques", 
        "Serviettes en papier", 
        "Déchets alimentaires",
        "Fruits entamés",
        "Le pain",
        "TOTAL GÉNÉRAL"
    ],
    "Quantité (kg)": [
        f"{infos['plastique']} kg", 
        f"{infos['serviettes']} kg", 
        f"{infos['alimentaire']} kg",
        f"{infos['fruits']} kg",
        f"{infos['pain']} kg",
        f"{total:.1f} kg"
    ]
}

st.table(tableau)

st.markdown("---")
# Bouton vers le Google Sheets
st.write("📖 Pour voir toutes les données historiques :")
st.link_button("📂 Ouvrir le tableau Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
