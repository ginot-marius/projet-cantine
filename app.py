import streamlit as st

# Titre principal
st.title("📊 Grand Suivi des Déchets - Établissements Scolaires")
st.write("Projet CDSG - Visualisation des données de pesée")

st.markdown("---")

# 1. BASE DE DONNÉES (Exemple à remplacer avec tes vraies données du Google Sheets)
# Tu me donneras tes vrais chiffres et je les changerai ici !
donnees_etablissements = {
    "Collège du Vaucluse": {"serviettes": 1.2, "pain": 4.5, "emballages": 2.1, "fruits": 3.0, "alimentaires": 12.4},
    "Collège Jean Moulin": {"serviettes": 0.8, "pain": 3.2, "emballages": 1.5, "fruits": 2.1, "alimentaires": 9.0},
    "Lycée Lumière": {"serviettes": 2.5, "pain": 8.0, "emballages": 4.2, "fruits": 5.5, "alimentaires": 22.1},
    "Lycée Professionnel Denis Diderot": {"serviettes": 1.9, "pain": 6.1, "emballages": 3.0, "fruits": 4.0, "alimentaires": 15.3},
    "École Primaire Centre": {"serviettes": 0.5, "pain": 2.0, "emballages": 1.0, "fruits": 1.5, "alimentaires": 5.0},
    "Université de Franche-Comté": {"serviettes": 5.0, "pain": 15.4, "emballages": 9.1, "fruits": 10.0, "alimentaires": 45.8}
}

# 2. CHOIX DE L'ÉTABLISSEMENT
st.header("🏫 Sélection de l'établissement")
liste_etablissements = list(donnees_etablissements.keys())
etablissement_choisi = st.selectbox("Choisissez une école, un collège, un lycée ou une université :", liste_etablissements)

# Récupération des données de l'établissement choisi
infos = donnees_etablissements[etablissement_choisi]

# Calcul du total
total_dechets = infos["serviettes"] + infos["pain"] + infos["emballages"] + infos["fruits"] + infos["alimentaires"]

st.markdown("---")

# 3. AFFICHAGE DES DONNÉES SOUS FORME DE TABLEAU
st.header(f"📋 Données enregistrées - {etablissement_choisi}")

tableau_affichage = {
    "Catégorie de Poubelle": [
        "1. Serviettes papiers", 
        "2. Le pain", 
        "3. Les emballages", 
        "4. Fruits entamés", 
        "5. Déchets alimentaires",
        "TOTAL GÉNÉRAL"
    ],
    "Poids (en kg)": [
        f"{infos['serviettes']:.1f} kg", 
        f"{infos['pain']:.1f} kg", 
        f"{infos['emballages']:.1f} kg", 
        f"{infos['fruits']:.1f} kg", 
        f"{infos['alimentaires']:.1f} kg",
        f"{total_dechets:.1f} kg"
    ]
}

# Affichage du tableau propre
st.table(tableau_affichage)

st.markdown("---")

# 4. LIEN VERS LE TABLEAU EN LIGNE
st.write("🔗 Lien direct vers la source :")
st.link_button("📂 Ouvrir le Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
