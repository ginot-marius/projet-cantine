import streamlit as st
import pandas as pd
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Saisie & Sauvegarde Déchets", page_icon="📝", layout="centered")

st.title("📝 Saisie et Sauvegarde des Pesées")
st.write("Les données sont sauvegardées automatiquement dans l'application et ne disparaissent pas.")

st.markdown("---")

# 2. LISTE OFFICIELLE DES 19 ÉTABLISSEMENTS
liste_etablissements = [
    "COLLEGE J. GIONO", "LYCEE DE L'ARC", "COLLEGE ARAUSIO", "LP ARGENSOL", 
    "COLLEGE B. HENDRICKS", "LP A. BRIAND", "LYCEE VITICOLE", "ENSEMBLE SCOLAIRE SAINT LOUIS", 
    "LYCEE L. AUBRAC", "COLLEGE H. BOUDON", "COLLEGE P. ELUARD", "COLLEGE VALLIS AERIA", 
    "LP F. REVOUL", "ES SAINT-JEAN-LE -BAPTISTE", "COLLEGE V. SCHOELCHER", "COLLEGE SAINT-EXUPERY", 
    "école Jules Ferry", "école du grillon", "école curie"
]

FICHIER_SAUVEGARDE = "sauvegarde_dechets.csv"

# Fonction pour générer un tableau tout neuf à 0
def generer_tableau_vierge():
    donnees_initiales = {
        "Établissement": liste_etablissements,
        "Emballages plastiques (kg)": [0.0] * len(liste_etablissements),
        "Serviettes en papier (kg)": [0.0] * len(liste_etablissements),
        "Déchets alimentaires (kg)": [0.0] * len(liste_etablissements),
        "Fruits entamés (kg)": [0.0] * len(liste_etablissements),
        "Le pain (kg)": [0.0] * len(liste_etablissements),
        "TOTAL (kg)": [0.0] * len(liste_etablissements)
    }
    df = pd.DataFrame(donnees_initiales).set_index("Établissement")
    df.to_csv(FICHIER_SAUVEGARDE)
    return df

# 3. CHARGEMENT OU INITIALISATION DU FICHIER
if os.path.exists(FICHIER_SAUVEGARDE):
    df_global = pd.read_csv(FICHIER_SAUVEGARDE, index_col="Établissement")
    for etab in liste_etablissements:
        if etab not in df_global.index:
            df_global.loc[etab] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
else:
    df_global = generer_tableau_vierge()

# 4. FORMULAIRE DE SAISIE
st.header("📥 Enregistrer une nouvelle pesée")
with st.form("formulaire_pesee", clear_on_submit=True):
    etablissement = st.selectbox("Sélectionnez l'établissement :", liste_etablissements)
    
    col1, col2 = st.columns(2)
    with col1:
        plastique = st.number_input("1. Emballages plastiques (kg)", min_value=0.0, step=0.1, format="%.2f")
        serviettes = st.number_input("2. Les serviettes en papier (kg)", min_value=0.0, step=0.1, format="%.2f")
        alimentaire = st.number_input("3. Les déchets alimentaires (kg)", min_value=0.0, step=0.1, format="%.2f")
    with col2:
        fruits = st.number_input("4. Les fruits entamés (kg)", min_value=0.0, step=0.1, format="%.2f")
        pain = st.number_input("5. Le pain (kg)", min_value=0.0, step=0.1, format="%.2f")
    
    bouton_valider = st.form_submit_button("💾 Enregistrer et Sauvegarder")

if bouton_valider:
    total_etablissement = plastique + serviettes + alimentaire + fruits + pain
    df_global.loc[etablissement] = [plastique, serviettes, alimentaire, fruits, pain, total_etablissement]
    df_global.to_csv(FICHIER_SAUVEGARDE)
    st.success(f"✅ Données sauvegardées pour : **{etablissement}** !")
    st.rerun()

st.markdown("---")

# 5. LE DEUXIÈME TABLEAU : RÉCAPITULATIF PERMANENT
st.header("📊 Tableau de bord général des établissements")
st.dataframe(df_global, use_container_width=True)

st.markdown("---")

# 6. ZONE DE RÉINITIALISATION SÉCURISÉE
st.subheader("⚠️ Zone d'administration (Réservée)")
st.write("Pour réinitialiser le tableau, entrez le code secret ci-dessous :")

# Case pour taper le code secret (les caractères seront masqués)
code_saisi = st.text_input("Entrez le code de sécurité :", type="password")

if st.button("♻️ Confirmer la réinitialisation générale"):
    if code_saisi == "CDSG":
        df_global = generer_tableau_vierge()
        st.success("🔄 Tout le tableau a été remis à zéro avec succès !")
        st.rerun()
    elif code_saisi == "":
        st.warning("Veuillez d'abord saisir le code secret.")
    else:
        st.error("❌ Code incorrect ! Action refusée.")

st.markdown("---")
st.link_button("📂 Ouvrir le fichier Google Sheets d'origine", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
