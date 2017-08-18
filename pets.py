class Pet(object):
    def __init__ (self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.get_species

    def __str__(self):
        return "{} is a {}". format(self.name, self.get_species)
    
class Dog(Pet):
    def __init__ (self, name, chases_cats):
        Pet.__init__(self, name, 'Dog')
        self.chases_cats = chases_cats

    def chases_cats(self):
        return self.chases_cats

class Cat(Pet):
    def __init__ (self, name, hates_dogs):
        Pet.__init__(self, name, 'Cat')
        self.hates_dogs = hates_dogs

    def is_hates_dogs(self):
        return self.hates_dogs

    def say_something(self):
        print "Meow Meow !!!"
