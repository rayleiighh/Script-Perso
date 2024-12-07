import unittest
import os
import pandas as pd
from src.recherche import rechercher_donnees

class TestRecherche(unittest.TestCase):
    def setUp(self):
        """Prépare un fichier CSV consolidé d'exemple pour les tests."""
        self.test_data_dir = "../tests/temp_data"
        os.makedirs(self.test_data_dir, exist_ok=True)

        self.fichier_consolide = os.path.join(self.test_data_dir, "consolidated_test.csv")

        # Données d'exemple
        data = {
            "Produit": ["Pomme", "Banane", "Pomme", "Orange"],
            "Quantité": [10, 20, 15, 25],
            "Prix Unitaire": [0.5, 0.3, 0.5, 0.8]
        }
        pd.DataFrame(data).to_csv(self.fichier_consolide, index=False)

    def tearDown(self):
        """Nettoie les fichiers générés après les tests."""
        if os.path.exists(self.fichier_consolide):
            os.remove(self.fichier_consolide)

    def test_recherche_produit(self):
        """Teste la recherche par nom de produit."""
        result = rechercher_donnees(self.fichier_consolide, "Produit", "Pomme")
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)  # Deux lignes pour "Pomme"

    def test_recherche_quantite(self):
        """Teste la recherche par quantité."""
        result = rechercher_donnees(self.fichier_consolide, "Quantité", 15)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)  # Une ligne avec Quantité <= 15

    def test_colonne_invalide(self):
        """Teste la recherche avec une colonne inexistante."""
        result = rechercher_donnees(self.fichier_consolide, "Categorie", "Fruit")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
