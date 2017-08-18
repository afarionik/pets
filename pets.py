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
