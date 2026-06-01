import streamlit as st

# Titre principal de l'application
st.title("📊 Suivi des déchets des cantines - CDSG")
st.write("Application de suivi et de comparaison des pesées de déchets.")

st.markdown("---")

# 1. CHOIX DU COLLÈGE
st.header("🏫 Sélection de l'établissement")
college_choisi = st.selectbox(
    "Pour quel collège souhaitez-vous saisir ou voir les données ?",
    [
        "Collège du Vaucluse", 
        "Collège Jean Moulin", 
        "Collège Jules Verne", 
        "Collège Pasteur"
    ]
)

st.success(f"Vous modifiez actuellement les données pour : **{college_choisi}**")

st.markdown("---")

# 2. RENTRER LES CHIFFRES DE LA PESÉE
st.header(f"⚖️ Pesée du jour (en kg) - {college_choisi}")

# On crée 5 cases de saisie pour le collège sélectionné
serviettes = st.number_input("Poubelle 1 : Serviettes papiers (kg)", min_value=0.0, step=0.1, key="serviettes")
pain = st.number_input("Poubelle 2 : Le pain (kg)", min_value=0.0, step=0.1, key="pain")
emballages = st.number_input("Poubelle 3 : Les emballages (kg)", min_value=0.0, step=0.1, key="emballages")
fruits = st.number_input("Poubelle 4 : Fruits entamés (kg)", min_value=0.0, step=0.1, key="fruits")
alimentaires = st.number_input("Poubelle 5 : Déchets alimentaires (kg)", min_value=0.0, step=0.1, key="alimentaires")

# Calcul du total
total_dechets = serviettes + pain + emballages + fruits + alimentaires

st.markdown("---")

# 3. AFFICHAGE SOUS FORME DE TABLEAU
st.header("📋 Tableau récapitulatif de la pesée")

# On fabrique un joli tableau avec les données pour l'afficher à l'écran
donnees_tableau = {
    "Catégorie de Poubelle": [
        "1. Serviettes papiers", 
        "2. Le pain", 
        "3. Les emballages", 
        "4. Fruits entamés", 
        "5. Déchets alimentaires",
        "TOTAL GÉNÉRAL"
    ],
    "Poids enregistré (en kg)": [
        f"{serviettes:.1f} kg", 
        f"{pain:.1f} kg", 
        f"{emballages:.1f} kg", 
        f"{fruits:.1f} kg", 
        f"{alimentaires:.1f} kg",
        f"{total_dechets:.1f} kg"
    ]
}

# Streamlit affiche le dictionnaire sous forme de vrai tableau propre
st.table(donnees_tableau)
st.markdown("---")

# 4. LIEN VERS LE GRAND TABLEAU EN LIGNE
st.header("🔗 Historique global")
st.write("Cliquez ci-dessous pour ouvrir le grand tableau de suivi partagé :")
st.link_button("📂 Ouvrir le Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
