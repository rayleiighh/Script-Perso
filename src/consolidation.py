import pandas as pd
import os
import logging

# Configurer les logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../outputs/consolidation.log"),
        logging.StreamHandler()
    ]
)

def consolider_fichiers_csv(fichiers_csv, output_path="../outputs/consolidated.csv"):
    """
    Consolide plusieurs fichiers CSV en un seul fichier.

    Args:
        fichiers_csv (list): Liste des chemins des fichiers CSV à consolider.
        output_path (str): Chemin du fichier CSV de sortie.

    Returns:
        bool: True si la consolidation a réussi, False sinon.
    """
    try:
        # Vérifier si la liste de fichiers est vide
        if not fichiers_csv:
            logging.error("Aucun fichier CSV fourni pour la consolidation.")
            return False

        # Charger et valider chaque fichier
        dataframes = []
        for fichier in fichiers_csv:
            if not os.path.exists(fichier):
                logging.error(f"Le fichier '{fichier}' est introuvable.")
                return False
            try:
                df = pd.read_csv(fichier)
                dataframes.append(df)
                logging.info(f"Chargé : {fichier}")
            except Exception as e:
                logging.error(f"Erreur lors de la lecture du fichier '{fichier}': {e}")
                return False

        # Vérifier que tous les fichiers ont les mêmes colonnes
        colonnes_reference = dataframes[0].columns
        for i, df in enumerate(dataframes):
            if not df.columns.equals(colonnes_reference):
                logging.error(f"Les colonnes du fichier {fichiers_csv[i]} ne correspondent pas.")
                return False

        # Fusionner les fichiers CSV
        data_consolidee = pd.concat(dataframes, ignore_index=True)
        logging.info("Fusion des fichiers CSV réussie.")

        # Sauvegarder le fichier consolidé
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data_consolidee.to_csv(output_path, index=False)
        logging.info(f"Fichier consolidé enregistré : {output_path}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        return False
