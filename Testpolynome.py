import unittest
from script import *

class TestSecondDegreePolynomial(unittest.TestCase):
    """Classe de tests unitaires pour la fonction second_degree_polynomial."""
    
    def test_discriminant_negative(self):
        self.assertEqual(second_degree_polynomial(1, 2, 3), "null")
    
    def test_discriminant_zero(self):
        self.assertEqual(second_degree_polynomial(1, -2, 1), (1.0,))
    
    def test_discriminant_positive(self):
        self.assertEqual(second_degree_polynomial(1, -5, 6), (3.0, 2.0))
    
    def test_discriminant_None(self):
        self.assertEqual(second_degree_polynomial(), None)

if __name__ == '__main__':
    unittest.main()