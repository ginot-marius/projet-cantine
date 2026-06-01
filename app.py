import streamlit as st

# Titre principal de l'application
st.title("📊 Grand Suivi des Déchets - Projet EPLE bas carbone")
st.write("Application officielle de visualisation et de suivi des données de pesée.")

st.markdown("---")

# 1. BASE DE DONNÉES OFFICIELLE DES 21 ÉTABLISSEMENTS AVEC LES 5 POUBELLES
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

# 2. SÉLECTION DE L'ÉTABLISSEMENT
st.header("🏫 Sélection de l'établissement")
liste_etablissements = list(donnees_etablissements.keys())
etablissement_choisi = st.selectbox("Choisissez l'établissement à analyser :", liste_etablissements)

# Récupération des données associées
infos = donnees_etablissements[etablissement_choisi]

# Calcul du total des déchets pour cet établissement
total_dechets = infos["plastique"] + infos["serviettes"] + infos["alimentaire"] + infos["fruits"] + infos["pain"]

st.markdown("---")

# 3. AFFICHAGE DU TABLEAU DE BORD AVEC LES BONS NOMS DE POUBELLES
st.header(f"📋 Tableau récapitulatif - {etablissement_choisi}")

tableau_affichage = {
    "Poubelles de Tri": [
        "Emballages plastiques", 
        "Les serviettes en papier", 
        "Les déchets alimentaires",
        "Les fruits entamés",
        "Le pain",
        "TOTAL DES DÉCHETS RELEVÉS"
    ],
    "Quantité (en kg)": [
        f"{infos['plastique']:.1f} kg", 
        f"{infos['serviettes']:.1f} kg", 
        f"{infos['alimentaire']:.1f} kg",
        f"{infos['fruits']:.1f} kg",
        f"{infos['pain']:.1f} kg",
        f"{total_dechets:.1f} kg"
    ]
}

# Affichage sous forme de tableau Streamlit propre
st.table(tableau_affichage)

st.markdown("---")

# 4. LIEN VERS LE GOOGLE SHEETS ORIGINAL
st.header("🔗 Lien Source")
st.write("Accéder au document complet 'Projet EPLE bas carbone' :")
st.link_button("📂 Ouvrir le Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
