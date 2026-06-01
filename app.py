import streamlit as st

# Titre principal de l'application
st.title("📊 Grand Suivi des Déchets - Projet EPLE bas carbone")
st.write("Application officielle de visualisation et de suivi des données de pesée.")

st.markdown("---")

# 1. BASE DE DONNÉES OFFICIELLE DES 21 ÉTABLISSEMENTS (Extraite de ton Google Sheets)
donnees_etablissements = {
    "COLLEGE J. GIONO": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LYCEE DE L'ARC": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE ARAUSIO": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LP ARGENSOL": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE B. HENDRICKS": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LP A. BRIAND": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LYCEE VITICOLE": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "ENSEMBLE SCOLAIRE SAINT LOUIS": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LYCEE L. AUBRAC": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE H. BOUDON": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE P. ELUARD": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE VALLIS AERIA": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "LP F. REVOUL": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "ES SAINT-JEAN-LE -BAPTISTE": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE V. SCHOELCHER": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "COLLEGE SAINT-EXUPERY": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "école Jules Ferry": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "école du grillon": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0},
    "école curie": {"plastique": 0.0, "papier": 0.0, "alimentaire": 0.0}  # Chiffres du tableau
}

# 2. SÉLECTION DE L'ÉTABLISSEMENT
st.header("🏫 Sélection de l'établissement")
liste_etablissements = list(donnees_etablissements.keys())
etablissement_choisi = st.selectbox("Choisissez l'établissement à analyser :", liste_etablissements)

# Récupération des données associées
infos = donnees_etablissements[etablissement_choisi]

# Calcul du total des déchets pour cet établissement
total_dechets = infos["plastique"] + infos["papier"] + infos["alimentaire"]

st.markdown("---")

# 3. AFFICHAGE DU TABLEAU DE BORD
st.header(f"📋 Tableau récapitulatif - {etablissement_choisi}")

tableau_affichage = {
    "Catégorie de Déchets": [
        "Plastique", 
        "Papier", 
        "Déchets Alimentaires",
        "TOTAL DES DÉCHETS RELEVÉS"
    ],
    "Quantité / Impact": [
        f"{infos['plastique']:.2f}", 
        f"{infos['papier']:.2f}", 
        f"{infos['alimentaire']:.2f}",
        f"{total_dechets:.2f}"
    ]
}

# Affichage sous forme de tableau Streamlit propre
st.table(tableau_affichage)

st.markdown("---")

# 4. LIEN VERS LE GOOGLE SHEETS ORIGINAL
st.header("🔗 Lien Source")
st.write("Accéder au document complet 'Projet EPLE bas carbone' :")
st.link_button("📂 Ouvrir le Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
