import pandas as pd
import logging
import os

# Créer le dossier 'outputs' s'il n'existe pas
os.makedirs("../outputs", exist_ok=True)
# Configurer les logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../outputs/recherche.log"),
        logging.StreamHandler()
    ]
)

def rechercher_donnees(fichier_consolide, filtre, valeur):
    """
    Recherche des données dans un fichier consolidé en fonction d'un filtre.

    Args:
        fichier_consolide (str): Chemin du fichier CSV consolidé.
        filtre (str): Colonne à filtrer (ex : 'Produit', 'Prix Unitaire').
        valeur (str, int, float): Valeur du filtre.

    Returns:
        pd.DataFrame or None: Résultats de la recherche ou None si erreur.
    """
    try:
        # Charger le fichier consolidé
        df = pd.read_csv(fichier_consolide)

        # Vérifier si le filtre existe
        if filtre not in df.columns:
            logging.error(f"Le filtre '{filtre}' n'existe pas dans le fichier.")
            return None

        # Appliquer le filtre
        if isinstance(valeur, (int, float)):
            resultats = df[df[filtre] == valeur]  # Égalité stricte
        else:
            resultats = df[df[filtre].str.contains(valeur, case=False, na=False)]

        logging.info(f"Recherche effectuée avec succès : {len(resultats)} résultats trouvés.")
        return resultats

    except Exception as e:
        logging.error(f"Erreur lors de la recherche : {e}")
        return None
