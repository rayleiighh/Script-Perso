# Gestion d'inventaire
Ce programme permet de consolider des fichiers CSV, rechercher des informations et générer un rapport récapitulatif.

## Installation
- Clonez le dépôt Git.
- Installez les dépendances :
  ```bash
  pip install -r requirements.txt

## Utilisation
- S'assurer que tous les fichiers soient aux bons endroits pour éviter de créer des erreurs au niveau des chemins utilisés dans les différents fichiers.
- Lancer le `main.py`.
- Vérifier que les fichiers `consolidated.csv`, `consolidation.log` et `rapport.csv` affichent correctement les résultats attendus.
- Regarder aussi dans le terminal s'il affiche correctement les `[INFO]` attendus dans les fichiers mentionnés juste au-dessus.
  - Changer les valeurs dans le `main.py` pour faire varier les rapports dans cette zone:
      ```python 
        fichier_consolide = "../outputs/consolidated.csv"
        filtre = "Produit"
        valeur = "Pomme"
  