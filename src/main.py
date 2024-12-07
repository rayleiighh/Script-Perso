from src.consolidation import consolider_fichiers_csv
from src.recherche import rechercher_donnees
from src.rapport import generer_rapport

if __name__ == "__main__":
    # Consolidation des fichiers
    fichiers_csv = ["../data/categorie1.csv", "../data/categorie2.csv"]
    success = consolider_fichiers_csv(fichiers_csv)
    if success:
        print("Consolidation terminée avec succès.")
    else:
        print("Échec de la consolidation.")

    # Recherche rapide
    fichier_consolide = "../outputs/consolidated.csv"
    filtre = "Produit"
    valeur = "Pomme"
    resultats = rechercher_donnees(fichier_consolide, filtre, valeur)

    if resultats is not None:
        print(resultats)
    else:
        print("Aucun résultat trouvé ou une erreur est survenue.")

    # Génération de rapport
    success = generer_rapport(fichier_consolide)
    if success:
        print("Rapport généré avec succès.")
    else:
        print("Une erreur est survenue lors de la génération du rapport.")
