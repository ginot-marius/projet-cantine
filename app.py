import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Saisie & Graphique Déchets", page_icon="📝", layout="centered")

st.title("📝 Saisie et Répartition Globale des Déchets")
st.write("Enregistrez les pesées pour mettre à jour le graphique circulaire en temps réel.")

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

# 5. LE NOUVEAU GRAPHIQUE CIRCULAIRE (À la place du grand tableau)
st.header("📊 Répartition globale des poubelles (Tous établissements)")

# Calcul du total général de chaque poubelle pour le graphique
somme_plastique = df_global["Emballages plastiques (kg)"].sum()
somme_serviettes = df_global["Serviettes en papier (kg)"].sum()
somme_alimentaire = df_global["Déchets alimentaires (kg)"].sum()
somme_fruits = df_global["Fruits entamés (kg)"].sum()
somme_pain = df_global["Le pain (kg)"].sum()

total_general_tous_dechets = somme_plastique + somme_serviettes + somme_alimentaire + somme_fruits + somme_pain

# Sécurité : Si le tableau est totalement vide (0 kg partout), on n'affiche pas un graphique blanc d'erreur
if total_general_tous_dechets == 0:
    st.info("💡 Le graphique circulaire s'affichera ici dès qu'une première pesée sera enregistrée dans le formulaire.")
else:
    # Préparation des données du graphique
    categories = [
        "Emballages plastiques", 
        "Serviettes en papier", 
        "Déchets alimentaires", 
        "Fruits entamés", 
        "Le pain"
    ]
    valeurs = [somme_plastique, somme_serviettes, somme_alimentaire, somme_fruits, somme_pain]
    
    # Choix des couleurs demandées pour chaque poubelle
    couleurs = [
        "#5499C7",  # Bleu pour le plastique
        "#A6ACAF",  # Gris pour les serviettes
        "#52BE80",  # Vert pour les déchets alimentaires
        "#F4D03F",  # Jaune/Orange pour les fruits
        "#DC7633"   # Marron/Pain cuit pour le pain
    ]
    
    # Création de la figure Matplotlib
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Génération du camembert
    wedges, texts, autotexts = ax.pie(
        valeurs, 
        labels=categories, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=couleurs,
        textprops=dict(color="black", fontweight="bold")
    )
    
    # Style des petits textes de pourcentages à l'intérieur
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)

    ax.axis('equal')  # Force le graphique à être un cercle parfait
    
    # Affichage du graphique dans Streamlit
    st.pyplot(fig)
    
    # Petit récapitulatif textuel des kilogrammes juste en dessous
    st.write(f"**Quantités totales collectées (Somme de tous les établissements) :**")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.write(f"🔵 Plastiques : **{somme_plastique:.2f} kg**")
        st.write(f"⚪ Serviettes : **{somme_serviettes:.2f} kg**")
    with col_b:
        st.write(f"🟢 Alimentaire : **{somme_alimentaire:.2f} kg**")
        st.write(f"🟡 Fruits : **{somme_fruits:.2f} kg**")
    with col_c:
        st.write(f"🟤 Pain : **{somme_pain:.2f} kg**")
        st.write(f"📊 **TOTAL GLOBAL : {total_general_tous_dechets:.2f} kg**")

st.markdown("---")

# 6. ZONE DE RÉINITIALISATION SÉCURISÉE (CODE : CDSG)
st.subheader("⚠️ Zone d'administration (Réservée)")
st.write("Pour remettre le graphique et les données à zéro, entrez le code secret :")

code_saisi = st.text_input("Entrez le code de sécurité :", type="password")

if st.button("♻️ Confirmer la réinitialisation générale"):
    if code_saisi == "CDSG":
        df_global = generer_tableau_vierge()
        st.success("🔄 Tout a été remis à zéro avec succès ! Le graphique est réinitialisé.")
        st.rerun()
    elif code_saisi == "":
        st.warning("Veuillez d'abord saisir le code secret.")
    else:
        st.error("❌ Code incorrect ! Action refusée.")
