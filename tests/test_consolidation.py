import unittest
import os
import pandas as pd
from src.consolidation import consolider_fichiers_csv

class TestConsolidation(unittest.TestCase):

    def setUp(self):
        """Prépare des fichiers CSV d'exemple pour les tests."""
        os.makedirs("tests/temp_data", exist_ok=True)
        self.file1 = "tests/temp_data/test_categorie1.csv"
        self.file2 = "tests/temp_data/test_categorie2.csv"
        self.output_file = "tests/temp_data/consolidated_test.csv"

        data1 = {"Produit": ["Pomme", "Banane"], "Quantité": [10, 20], "Prix Unitaire": [0.5, 0.3]}
        data2 = {"Produit": ["Tomate", "Carotte"], "Quantité": [30, 40], "Prix Unitaire": [0.8, 0.5]}
        pd.DataFrame(data1).to_csv(self.file1, index=False)
        pd.DataFrame(data2).to_csv(self.file2, index=False)

    def tearDown(self):
        """Nettoie les fichiers temporaires après les tests."""
        if os.path.exists(self.file1):
            os.remove(self.file1)
        if os.path.exists(self.file2):
            os.remove(self.file2)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_consolidation_reussie(self):
        """Teste la consolidation avec des fichiers valides."""
        success = consolider_fichiers_csv([self.file1, self.file2], self.output_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(self.output_file))

        # Vérifie le contenu du fichier consolidé
        df = pd.read_csv(self.output_file)
        self.assertEqual(len(df), 4)  # 2 lignes de chaque fichier

    def test_fichier_manquant(self):
        """Teste la gestion des fichiers manquants."""
        success = consolider_fichiers_csv(["tests/temp_data/inexistant.csv"], self.output_file)
        self.assertFalse(success)

    def test_colonnes_differentes(self):
        """Teste la gestion des fichiers avec des colonnes différentes."""
        data_diff = {"Nom": ["ProduitX"], "Valeur": [50]}
        file_diff = "tests/temp_data/test_diff.csv"
        pd.DataFrame(data_diff).to_csv(file_diff, index=False)

        success = consolider_fichiers_csv([self.file1, file_diff], self.output_file)
        self.assertFalse(success)

        os.remove(file_diff)

if __name__ == "__main__":
    unittest.main()
