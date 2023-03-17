import unittest
from td1_cours import *


class TestFonctions(unittest.TestCase):

    def test_generer_mot_de_passe_defaut(self):
        mot_de_passe = generer_mot_de_passe()
        self.assertEqual(len(mot_de_passe), 12)

    def test_generer_mot_de_passe_longueur_personnalisee(self):
        mot_de_passe = generer_mot_de_passe(taille=16)
        self.assertEqual(len(mot_de_passe), 16)

    def test_generer_mot_de_passe_sans_caracteres_speciaux(self):
        mot_de_passe = generer_mot_de_passe(taille=16, caracteres_speciaux=False)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in mot_de_passe))

    def test_generer_mot_de_passe_longueur_1(self):
        mot_de_passe = generer_mot_de_passe(taille=1)
        self.assertEqual(len(mot_de_passe), 1)

    def test_generer_mot_de_passe_longueur_1_sans_caracteres_speciaux(self):
        mot_de_passe = generer_mot_de_passe(taille=1, caracteres_speciaux=False)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in mot_de_passe))

    def test_texte_vers_morse_lettres(self):
        texte = "hello"
        morse = texte_vers_morse(texte)
        self.assertEqual(morse, ".... . .-.. .-.. ---")

    def test_texte_vers_morse_chiffres(self):
        texte = "12345"
        morse = texte_vers_morse(texte)
        self.assertEqual(morse, ".---- ..--- ...-- ....- .....")

    def test_texte_vers_morse_lettres_chiffres_espaces(self):
        texte = "Hello 123"
        morse = texte_vers_morse(texte)
        self.assertEqual(morse, ".... . .-.. .-.. --- / .---- ..--- ...--")

    def test_texte_vers_morse_lettres_majuscules(self):
        texte = "Hello"
        morse = texte_vers_morse(texte)
        self.assertEqual(morse, ".... . .-.. .-.. ---")

    def test_texte_vers_morse_caracteres_non_pris_en_charge(self):
        texte = "Hello !"
        morse = texte_vers_morse(texte)
        self.assertEqual(morse, ".... . .-.. .-.. --- / ?")


if __name__ == "__main__":
    unittest.main()
