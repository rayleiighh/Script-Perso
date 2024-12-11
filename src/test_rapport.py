import unittest
import os
import pandas as pd
from rapport import generer_rapport

class TestRapport(unittest.TestCase):
    def setUp(self):
        """Prépare un fichier CSV consolidé d'exemple pour les tests."""
        self.outputs_dir = "../outputs"
        self.test_data_dir = "../tests/temp_data"
        os.makedirs(self.test_data_dir, exist_ok=True)

        self.fichier_consolide = os.path.join(self.test_data_dir, "consolidated_test.csv")
        self.fichier_rapport = os.path.join(self.outputs_dir, "rapport_test.csv")

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
        if os.path.exists(self.fichier_rapport):
            os.remove(self.fichier_rapport)

    def test_rapport_generation(self):
        """Teste la génération correcte du rapport."""
        success = generer_rapport(self.fichier_consolide, self.fichier_rapport)
        self.assertTrue(success)

        # Vérifie si le fichier rapport a été créé
        self.assertTrue(os.path.exists(self.fichier_rapport))

        # Vérifie le contenu du rapport
        rapport = pd.read_csv(self.fichier_rapport)
        expected_columns = ["Produit", "Quantité_Totale", "Valeur_Totale"]
        self.assertListEqual(list(rapport.columns), expected_columns)
        self.assertIn("TOTAL", rapport["Produit"].values)

    def test_rapport_donnees_correctes(self):
        """Vérifie que les données dans le rapport sont correctes."""
        generer_rapport(self.fichier_consolide, self.fichier_rapport)
        rapport = pd.read_csv(self.fichier_rapport)

        # Vérifie les valeurs par produit
        pomme = rapport[rapport["Produit"] == "Pomme"]
        self.assertEqual(pomme["Quantité_Totale"].iloc[0], 25)  # 10 + 15
        self.assertEqual(pomme["Valeur_Totale"].iloc[0], 12.5)  # 25 * 0.5

        # Vérifie la ligne TOTAL
        total_row = rapport[rapport["Produit"] == "TOTAL"]
        self.assertEqual(total_row["Quantité_Totale"].iloc[0], 70)  # 10 + 20 + 15 + 25

if __name__ == "__main__":
    unittest.main()
