

import unittest
from script import *

class TestMethods(unittest.TestCase):

    def test_create_identities_null(self):
        self.assertEqual(create_identities(11), None)
    
    def test_create_identities_no_duplicate(self):
        lst = create_identities(random.randint(1,10))
        self.assertFalse(len(lst) == len(set(lst)))


if __name__ == '__main__':
    unittest.main()