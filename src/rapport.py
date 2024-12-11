import pandas as pd
import os
import logging

# Créer le dossier 'outputs' s'il n'existe pas
os.makedirs("../outputs", exist_ok=True)
# Configurer les logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../outputs/rapport.log"),
        logging.StreamHandler()
    ]
)

def generer_rapport(fichier_consolide, fichier_sortie="../outputs/rapport.csv"):
    """
    Génère un rapport récapitulatif des stocks.

    Args:
        fichier_consolide (str): Chemin du fichier CSV consolidé.
        fichier_sortie (str): Chemin du fichier CSV de sortie.

    Returns:
        bool: True si le rapport a été généré avec succès, False sinon.
    """
    try:
        # Charger le fichier consolidé
        df = pd.read_csv(fichier_consolide)

        # Calculer les métriques
        stock_par_produit = df.groupby("Produit").agg(
            Quantité_Totale=("Quantité", "sum"),
            Valeur_Totale=("Prix Unitaire", lambda x: (x * df.loc[x.index, "Quantité"]).sum())
        )

        # Réinitialiser l'index pour inclure 'Produit' comme colonne
        stock_par_produit = stock_par_produit.reset_index()

        # Calculer les totaux globaux
        stock_total = stock_par_produit["Quantité_Totale"].sum()
        valeur_totale = stock_par_produit["Valeur_Totale"].sum()

        # Ajouter une ligne TOTAL
        total_row = pd.DataFrame(
            data={"Produit": ["TOTAL"], "Quantité_Totale": [stock_total], "Valeur_Totale": [valeur_totale]}
        )
        rapport = pd.concat([stock_par_produit, total_row], ignore_index=True)

        # Enregistrer le rapport sans sauvegarder l'index
        os.makedirs(os.path.dirname(fichier_sortie), exist_ok=True)
        rapport.to_csv(fichier_sortie, index=False)
        logging.info(f"Rapport généré avec succès : {fichier_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur lors de la génération du rapport : {e}")
        return False
