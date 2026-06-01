import streamlit as st

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Suivi Cantine - EPLE", page_icon="🥗", layout="centered")

# 2. PERSONNALISATION VISUELLE (CSS EN LIGNE)
st.markdown("""
    <style>
    /* Image de fond : Restaurant scolaire / Cantine */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }

    /* Bloc principal ultra-lisible et opaque pour les textes et tableaux */
    .main-box {
        background-color: #FFFFFF !important;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
        border: 2px solid #E0E0E0;
    }

    /* Force le texte standard en noir foncé pour un contraste maximum */
    .big-text {
        color: #111111 !important;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Titres principaux très visibles */
    h1 {
        color: #1E4620 !important;
        background-color: rgba(255, 255, 255, 0.95);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    h2, h3 {
        color: #1E4620 !important;
        font-weight: bold !important;
    }

    /* Application d'un fond blanc pur et de bordures nettes sur le tableau */
    .stTable, table {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 2px solid #1E4620 !important;
        border-collapse: collapse;
        width: 100%;
    }
    
    th {
        background-color: #1E4620 !important;
        color: white !important;
        font-weight: bold !important;
    }
    
    td {
        border: 1px solid #E0E0E0 !important;
        padding: 10px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENU DE L'APPLICATION
st.title("🥗 Grand Suivi des Déchets - CDSG")

# Premier bloc de texte
st.markdown("""
    <div class="main-box">
        <p class="big-text">
            Cette application permet de visualiser l'impact écologique de nos établissements du projet <b>EPLE bas carbone</b>. 
            Sélectionnez un établissement ci-dessous pour afficher le détail de ses pesées.
        </p>
    </div>
    """, unsafe_allow_html=True)

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

# Bloc Sélection de l'établissement
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.header("🏫 Établissement")
liste = list(donnees_etablissements.keys())
choix = st.selectbox("Choisir dans la liste :", liste)
st.markdown('</div>', unsafe_allow_html=True)

infos = donnees_etablissements[choix]
total = infos["plastique"] + infos["serviettes"] + infos["alimentaire"] + infos["fruits"] + infos["pain"]

# Bloc Résultats et Tableau
st.markdown('<div class="main-box">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# Bloc Lien Externe
st.markdown("""
    <div class="main-box">
        <h3>📖 Accès aux données globales</h3>
        <p class="big-text">Pour consulter ou modifier les feuilles de calcul d'origine :</p>
    </div>
    """, unsafe_allow_html=True)

st.link_button("📂 Ouvrir le tableau Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
