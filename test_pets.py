import unittest

from Pets import *

class TestPets(unittest.TestCase):

   def test_cats(self):
      cat = Cat(name="Kitty", hates_dogs=True)
      
      self.assertEqual("Kitty", cat.name)

   def test_dogs(self):
      dog = Dog(name="Bars", chases_cats=True)
      
      self.assertEqual("Bars", dog.chases_cats) 
      
if __name__=="__main__":
   unittest.main()
