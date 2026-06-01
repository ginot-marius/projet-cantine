import streamlit as st
import pandas as pd

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Formulaire & Récapitulatif - Cantine", page_icon="📝", layout="centered")

# 2. TITRE PRINCIPAL
st.title("📝 Saisie et Récapitulatif Global des Déchets")
st.write("Enregistrez les pesées pour mettre à jour automatiquement le grand tableau de bord.")

st.markdown("---")

# 3. LISTE DES 21 ÉTABLISSEMENTS
liste_etablissements = [
    "COLLEGE J. GIONO", "LYCEE DE L'ARC", "COLLEGE ARAUSIO", "LP ARGENSOL", 
    "COLLEGE B. HENDRICKS", "LP A. BRIAND", "LYCEE VITICOLE", "ENSEMBLE SCOLAIRE SAINT LOUIS", 
    "LYCEE L. AUBRAC", "COLLEGE H. BOUDON", "COLLEGE P. ELUARD", "COLLEGE VALLIS AERIA", 
    "LP F. REVOUL", "ES SAINT-JEAN-LE -BAPTISTE", "COLLEGE V. SCHOELCHER", "COLLEGE SAINT-EXUPERY", 
    "école Jules Ferry", "école du grillon", "école curie"
]

# 4. RÉINITIALISATION ET INITIALISATION DU TABLEAU GLOBAL (Tout est remis à 0)
# Cette structure crée un tableau propre et vierge avec des valeurs à 0.00
donnees_initiales = {
    "Établissement": liste_etablissements,
    "Emballages plastiques (kg)": [0.0] * len(liste_etablissements),
    "Serviettes en papier (kg)": [0.0] * len(liste_etablissements),
    "Déchets alimentaires (kg)": [0.0] * len(liste_etablissements),
    "Fruits entamés (kg)": [0.0] * len(liste_etablissements),
    "Le pain (kg)": [0.0] * len(liste_etablissements),
    "TOTAL (kg)": [0.0] * len(liste_etablissements)
}

if "df_global" not in st.session_state:
    st.session_state.df_global = pd.DataFrame(donnees_initiales).set_index("Établissement")

# Bouton de réinitialisation manuelle d'urgence (si besoin de vider le tableau en un clic)
if st.sidebar.button("♻️ Réinitialiser tout le tableau à zéro"):
    st.session_state.df_global = pd.DataFrame(donnees_initiales).set_index("Établissement")
    st.sidebar.success("Le tableau a été vidé !")

# 5. FORMULAIRE DE SAISIE
st.header("📥 Saisie d'une nouvelle pesée")
with st.form("formulaire_pesee", clear_on_submit=True):
    
    etablissement = st.selectbox("Sélectionnez l'établissement concerné :", liste_etablissements)
    
    col1, col2 = st.columns(2)
    with col1:
        plastique = st.number_input("1. Emballages plastiques (kg)", min_value=0.0, step=0.1, format="%.2f")
        serviettes = st.number_input("2. Les serviettes en papier (kg)", min_value=0.0, step=0.1, format="%.2f")
        alimentaire = st.number_input("3. Les déchets alimentaires (kg)", min_value=0.0, step=0.1, format="%.2f")
    with col2:
        fruits = st.number_input("4. Les fruits entamés (kg)", min_value=0.0, step=0.1, format="%.2f")
        pain = st.number_input("5. Le pain (kg)", min_value=0.0, step=0.1, format="%.2f")
    
    bouton_valider = st.form_submit_button("💾 Enregistrer cette pesée")

# 6. ENREGISTREMENT ET CALCULS LORS DU CLIC
if bouton_valider:
    total_etablissement = plastique + serviettes + alimentaire + fruits + pain
    
    # Mise à jour de la ligne de l'établissement
    st.session_state.df_global.loc[etablissement] = [
        plastique, 
        serviettes, 
        alimentaire, 
        fruits, 
        pain, 
        total_etablissement
    ]
    
    st.success(f"✅ Pesée mise à jour avec succès pour : **{etablissement}** (Total : {total_etablissement:.2f} kg)")

st.markdown("---")

# 7. LE DEUXIÈME TABLEAU : RÉCAPITULATIF GLOBAL RÉINITIALISÉ
st.header("📊 Tableau de bord général des établissements")
st.write("Ce tableau compile les dernières données enregistrées. Il n'est modifiable que via le formulaire ci-dessus.")

# Affichage du tableau de bord (qui repart à zéro)
st.dataframe(st.session_state.df_global, use_container_width=True)

st.markdown("---")

# 8. LIEN GOOGLE SHEETS
st.link_button("📂 Ouvrir le fichier Google Sheets complet", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
