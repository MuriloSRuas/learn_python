from typing import Union
from sys import exit

class Brawler(object):
    def __init__(self, name : str, life : int, damage : int, trait : Union[str , None]):
        self.name = name
        self.life = life
        self.damage = damage
        self.trait = trait
    class Attack(object):
        def __init__(self, name : str, damage : int):
            self.name = name
            self.damage = damage

    class BasicAttack(Attack):
        def __init__(self, name, damage):
            super().__init__(name, damage)
        def summary(self):
            return f"{self.name}\n\nThis attack cause {self.damage} of damage. {exit(0)}" 

    class SuperAttack(Attack):
        def __init__(self):
            super().__init__()

Chester = Brawler("Chester", 7000, 1200, "Yes")
print(Chester.BasicAttack("Bell and Hat", 1200).summary())