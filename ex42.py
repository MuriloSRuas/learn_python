class Creature:
    #Creature is-a class.
    def __init__(self, species : str, life : int, damage : int):
        self.species = species
        self.life = life
        self.damage = damage

class Human(Creature):
    #Human is-a Creature and has-a init and summary function; and the same attributes of Creature.
    def __init__(self, species, life, damage):
        super().__init__(species, life, damage)
        
    def summary(self):
        #Return Human attributes.
        return f"Specie: {self.species}, life: {self.life} and {self.damage}"

#The object "me" is-a Human and has-a specie, life and damage attributes.
me = Human(species="Human", life=20, damage=10)
print(me.summary())
