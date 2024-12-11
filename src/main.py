import argparse
from consolidation import consolider_fichiers_csv
from recherche import rechercher_donnees
from rapport import generer_rapport


def main():
    # Initialisation de argparse
    parser = argparse.ArgumentParser(description="Programme de gestion d'inventaire")
    parser.add_argument(
        "action",
        choices=["consolidation", "recherche", "rapport"],
        help="Action à effectuer : consolidation, recherche ou rapport"
    )
    parser.add_argument(
        "--fichiers",
        nargs="+",
        help="Liste des fichiers CSV à consolider (obligatoire pour 'consolidation')"
    )
    parser.add_argument(
        "--filtre",
        help="Nom de la colonne à utiliser pour la recherche (obligatoire pour 'recherche')"
    )
    parser.add_argument(
        "--valeur",
        help="Valeur à rechercher dans la colonne spécifiée (obligatoire pour 'recherche')"
    )
    parser.add_argument(
        "--sortie",
        help="Chemin du fichier de sortie pour le rapport (optionnel pour 'rapport')",
        default="../outputs/rapport.csv"
    )

    args = parser.parse_args()

    # Gestion des actions
    if args.action == "consolidation":
        if not args.fichiers:
            print("Erreur : Vous devez fournir une liste de fichiers avec --fichiers pour la consolidation.")
            return

        success = consolider_fichiers_csv(args.fichiers)
        if success:
            print("Consolidation terminée avec succès.")
        else:
            print("Échec de la consolidation.")

    elif args.action == "recherche":
        if not args.filtre or not args.valeur:
            print("Erreur : Vous devez fournir un filtre (--filtre) et une valeur (--valeur) pour la recherche.")
            return

        fichier_consolide = "../outputs/consolidated.csv"
        resultats = rechercher_donnees(fichier_consolide, args.filtre, args.valeur)
        if resultats is not None and not resultats.empty:
            print("Résultats de la recherche :")
            print(resultats)
        else:
            print("Aucun résultat trouvé ou une erreur est survenue.")

    elif args.action == "rapport":
        fichier_consolide = "../outputs/consolidated.csv"
        success = generer_rapport(fichier_consolide, args.sortie)
        if success:
            print(f"Rapport généré avec succès : {args.sortie}")
        else:
            print("Une erreur est survenue lors de la génération du rapport.")


if __name__ == "__main__":
    main()
