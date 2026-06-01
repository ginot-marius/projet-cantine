import streamlit as st

# Titre de la page
st.title("📊 Suivi des déchets de la cantine")
st.write("Projet CDSG - Collège du Vaucluse (700 demi-pensionnaires)")

st.markdown("---")

# Section pour entrer les données
st.header("⚖️ Pesée du jour (en kg)")

# On crée les 5 cases pour entrer les chiffres
serviettes = st.number_input("Poubelle 1 : Serviettes papiers (kg)", min_value=0.0, step=0.1)
pain = st.number_input("Poubelle 2 : Le pain (kg)", min_value=0.0, step=0.1)
emballages = st.number_input("Poubelle 3 : Les emballages (kg)", min_value=0.0, step=0.1)
fruits = st.number_input("Poubelle 4 : Fruits entamés (kg)", min_value=0.0, step=0.1)
alimentaires = st.number_input("Poubelle 5 : Déchets alimentaires (kg)", min_value=0.0, step=0.1)

st.markdown("---")

# Calcul du total avec les 5 poubelles
total_dechets = serviettes + pain + emballages + fruits + alimentaires

# Affichage du résultat
st.header("📈 Résultat")
st.metric(label="Total général des déchets", value=f"{total_dechets:.2f} kg")

st.markdown("---")

# Section Lien vers le Tableau Google Sheets
st.header("📋 Enregistrement des données")
st.write("Cliquez sur le bouton ci-dessous pour ouvrir le tableau de suivi et y reporter votre pesée :")

# Bouton de lien vers ton Google Sheets
st.link_button("📂 Ouvrir le tableau Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
