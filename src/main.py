from src.consolidation import consolider_fichiers_csv


if __name__ == "__main__":
    # Consolidation des fichiers
    fichiers_csv = ["../data/categorie1.csv", "../data/categorie2.csv"]
    success = consolider_fichiers_csv(fichiers_csv)
    if success:
        print("Consolidation terminée avec succès.")
    else:
        print("Échec de la consolidation.")
