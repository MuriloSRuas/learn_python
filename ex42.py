class Creature:
    #Creature is a class.
    def __init__(self, species : str, life : int, damage : int):
        self.species = species
        self.life = life
        self.damage = damage

class Human(Creature):
    def __init__(self, species, life, damage):
        super(Creature, self).__init__(species)
        self.life = life
        self.damage = damage
        
    def summary(self):
        return f"Specie: {Human.species}, life: {Human.life} and {Human.damage}"
        
me = Human("Human", 20, 10)
me.summary()