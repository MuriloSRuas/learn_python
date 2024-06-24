class Creature:
    #Creature is a class.
    def __init__(self, species : str, life : int, damage : int):
        self.species = species
        self.life = life
        self.damage = damage

class Human(Creature):
    def __init__(self, species, life, damage):
        super().__init__(species, life, damage)
        #This code doesn't work, error: TypeError: __init__() missing 3 required positional arguments: 'species', 'life', and 'damage'
        
    def summary(self):
        return f"Specie: {self.species}, life: {self.life} and {self.damage}"
        
me = Human(species="Human", life=20, damage=10)
print(me.summary())
