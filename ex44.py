from typing import Union
from sys import exit

class Brawler(object):
    def __init__(self, name : str, life : int, damage : int, trait : Union[str , None]):
        self.name = name
        self.life = life
        self.damage = damage
        self.trait = trait

    def summary(self):
        print(f"{self.name}\n\nLife: {self.life}\nDamage: {self.damage}\n Trait: {self.trait}")

Chester = Brawler("Chester", 7000, 1200, "Yes")
Chester.summary()