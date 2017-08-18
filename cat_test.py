import unittest

from QA_AF_pets import *

class TestPets(unittest.TestCase):

    def test_cats(self):
        
        cat=Cat(name='Kitty', hates_dogs=True)

        self.assertEqual("Kitty", cat.name)

if __name__ == '__main__':
    unittest.main()
