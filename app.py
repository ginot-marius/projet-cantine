import streamlit as st

# 1. CONFIGURATION DE LA PAGE (Simple et propre)
st.set_page_config(page_title="Formulaire de Saisie - Cantine", page_icon="📝", layout="centered")

# 2. TITRE PRINCIPAL
st.title("📝 Formulaire de Saisie des Consommations")
st.write("Remplissez les champs ci-dessous pour enregistrer les pesées du jour.")

st.markdown("---")

# 3. LISTE DES 21 ÉTABLISSEMENTS
liste_etablissements = [
    "COLLEGE J. GIONO", "LYCEE DE L'ARC", "COLLEGE ARAUSIO", "LP ARGENSOL", 
    "COLLEGE B. HENDRICKS", "LP A. BRIAND", "LYCEE VITICOLE", "ENSEMBLE SCOLAIRE SAINT LOUIS", 
    "LYCEE L. AUBRAC", "COLLEGE H. BOUDON", "COLLEGE P. ELUARD", "COLLEGE VALLIS AERIA", 
    "LP F. REVOUL", "ES SAINT-JEAN-LE -BAPTISTE", "COLLEGE V. SCHOELCHER", "COLLEGE SAINT-EXUPERY", 
    "école Jules Ferry", "école du grillon", "école curie"
]

# 4. CRÉATION DU FORMULAIRE DE SAISIE
with st.form("formulaire_pesee", clear_on_submit=True):
    
    st.subheader("🏫 Choix de l'établissement")
    etablissement = st.selectbox("Sélectionnez votre établissement :", liste_etablissements)
    
    st.markdown("---")
    st.subheader("⚖️ Quantités consommées / jetées (en kg)")
    
    # Les 5 poubelles demandées avec des cases pour taper les chiffres
    plastique = st.number_input("1. Emballages plastiques (kg)", min_value=0.0, step=0.1, format="%.2f")
    serviettes = st.number_input("2. Les serviettes en papier (kg)", min_value=0.0, step=0.1, format="%.2f")
    alimentaire = st.number_input("3. Les déchets alimentaires (kg)", min_value=0.0, step=0.1, format="%.2f")
    fruits = st.number_input("4. Les fruits entamés (kg)", min_value=0.0, step=0.1, format="%.2f")
    pain = st.number_input("5. Le pain (kg)", min_value=0.0, step=0.1, format="%.2f")
    
    st.markdown("---")
    
    # Bouton de validation à l'intérieur du formulaire
    bouton_valider = st.form_submit_button("💾 Valider et enregistrer la pesée")

# 5. TRAITEMENT DES DONNÉES APRÈS CLIC
if bouton_valider:
    # Calcul du total global
    total_general = plastique + serviettes + alimentaire + fruits + pain
    
    # Message de succès vert avec le récapitulatif
    st.success(f"✅ Données enregistrées avec succès pour l'établissement : **{etablissement}** !")
    
    # Affichage du résumé sous le formulaire
    st.info(f"""
    **Récapitulatif de la saisie :**
    * Emballages plastiques : {plastique:.2f} kg
    * Serviettes en papier : {serviettes:.2f} kg
    * Déchets alimentaires : {alimentaire:.2f} kg
    * Fruits entamés : {fruits:.2f} kg
    * Le pain : {pain:.2f} kg
    * **TOTAL GÉNÉRAL : {total_general:.2f} kg**
    """)

st.markdown("---")

# 6. LIEN VERS LE GOOGLE SHEETS
st.write("🔗 Pour consulter l'historique complet des saisies :")
st.link_button("📂 Ouvrir le tableau Google Sheets", "https://docs.google.com/spreadsheets/d/12fo8cluTH5DmI1dZJh2P_iJaso-NmplnEvxcyb5pS0M/edit?gid=169103083#gid=169103083")
