# Gestion d'inventaire
Ce programme permet de consolider des fichiers CSV, rechercher des informations et générer un rapport récapitulatif.

## Installation
- Clonez le dépôt Git.
- Installez les dépendances :
  ```bash
  pip install -r requirements.txt

## Utilisation
- S'assurer que tous les fichiers soient aux bons endroits pour éviter de créer des erreurs au niveau des chemins utilisés dans les différents fichiers.
- Vérifier que les fichiers `consolidated.csv`, `consolidation.log` et `rapport.csv` affichent correctement les résultats attendus.
- Utiliser ensuite ces lignes de commande dans la console pour tester les fonctions dans le `main.py` en étant bien vigilant faire un  `cd` src/ : 
  ```python
    python main.py consolidation --fichiers ../data/categorie1.csv ../data/categorie2.csv
    python main.py recherche --filtre Produit --valeur Pomme
    python main.py rapport --sortie ../outputs/rapport_personnalisé.csv

- Regarder aussi dans le terminal s'il affiche correctement les [INFO] attendus dans les fichiers mentionnés juste au-dessus.
