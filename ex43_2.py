from random import randint

#Classes

class Creature(object):
    def __init__(self, name : str, life : int, damage : int):
        self.name = name
        self.life = life
        self.damage = damage

class Dragon(Creature):
    def __init__(self):
        name = "Dragon"
        life = 30
        damage = 7
        super().__init__(name, life, damage)

    def attack(self, Player):
        hit = Dragon.damage + Dice.roll()
        Player.life = Player.life - hit
        return f"Damage: {hit}\n\nPlayer's life: {Player.life}"

    def dodge(self):
        
        dodge_rate = Dice()
        result = dodge_rate.roll(1, 101)

        if result < 50:
            
            print("Yeah!! It takes the damage!!")
            #It takes damage.

        elif result >= 50:
            
            #It dodges of your attack.
            print("Oh!! It dodged")

class Player(Creature):
    def __init__(self):
        life = 20
        damage = 5
        name = "Murilo"
        shield = 5

        super().__init__(name, life, damage)

        self.shield = shield

    def attack(self, Dragon):
        hit = self.damage + Dice.roll()
        Dragon.life = Dragon.life - hit
        return f"Damage: {hit} / Dragon's life: {Dragon.life}"

    def dodge(self, dice_roll, dragon_attack):
        if dice_roll >= dragon_attack:
            dodge = "Nice, you dodged!!"
            return dodge

        elif dice_roll < dragon_attack():
            dodge = "Ouch, you didn't dodged..."
            Player.life = (Player.life + Player.shield) - dragon_attack
            return dodge

    def protect():
        pass

class Dice(object):
    def roll(a, b):
        num = randint(a, b)
        return num
    
class Round():
    round = 1

    def __init__(self):
        self.Player = Player()

    def start(self):
        while round:
            print(f"Player\n\nLife: {Player.life}\nShield: {Player.shield}")
            break