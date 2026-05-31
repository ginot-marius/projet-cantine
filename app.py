import streamlit as st

# Titre de la page
st.title("📊 Suivi des déchets de la cantine")
st.write("Projet CDSG - Collège du Vaucluse (700 demi-pensionnaires)")

st.markdown("---")

# Section pour entrer les données
st.header("⚖️ Pesée du jour (en kg)")

# On crée 4 cases pour entrer les chiffres
serviettes = st.number_input("Poubelle 1 : Serviettes papiers (kg)", min_value=0.0, step=0.1)
pain = st.number_input("Poubelle 2 : Le pain (kg)", min_value=0.0, step=0.1)
emballages = st.number_input("Poubelle 3 : Les emballages (kg)", min_value=0.0, step=0.1)
fruits = st.number_input("Poubelle 4 : Fruits entamés (kg)", min_value=0.0, step=0.1)

st.markdown("---")

# Calcul du total
total_dechets = serviettes + pain + emballages + fruits

# Affichage du résultat
st.header("📈 Résultat")
st.metric(label="Total des déchets alimentaires", value=f"{total_dechets:.2f} kg")
