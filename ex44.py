from typing import Union

class Brawler(object):
    def __init__(self, name : str, life : int, damage : int, trait : Union[str , None]):
        self.name = name
        self.life = life
        self.damage = damage
        self.trait = trait

    def summary(self):
        print(f"{self.name}\n\nLife: {self.life}\nDamage: {self.damage}\n Trait: {self.trait}")

    def set_BasicAttack(self):
        name = input("What's the basic attack name?\n\n>")
        damage = int(input(f"What's the damage of {name}?\n\n>"))
        
        basic_attack = {
            "Name" : name,
            "Damage" : damage
        }

        print("Here is the informations:\n\n{}".format(basic_attack))
        return basic_attack

Chester = Brawler("Chester", 7000, 1200, "Yes")
Chester.set_BasicAttack()