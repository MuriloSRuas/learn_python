from random import randint

#Classes

class Creature(object):
    
    #Define the basic attributes of any Creature.

    def __init__(self, name : str, life : int, damage : int):

        #Any Creature has a name, life and damage.

        self.name = name
        self.life = life
        self.damage = damage

class Dragon(Creature):

    #Define a Dragon, that is a Creature.

    def __init__(self):

        #A Dragon is a Creature, then it has a name, life and damage too.
        name = "Dragon"
        life = 30
        damage = 7
        super().__init__(name, life, damage)

    #The Dragon 

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

    #Player is a Creature too, but the difference is the shield attribute. Only the Player has a shield.

    def __init__(self):
        
        life = 20
        damage = 5
        name = "Teichós"
        shield = 5

        super().__init__(name, life, damage)

        self.shield = shield

    #The Player can attack, dodge and protect himself. 

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
    
class Round(object):

    #It's the class Round, it init the round battles.

    def start(z, a : Player, b : Dragon):

        #Start a Round: a Vs b

        round = 1   #The Round always begins at 1.

        while round:
            
            print("**Round {}**\n".format(round))
            print(f"""
    {a.name}

    Life: {a.life}
    Shield: {a.shield}
                """)
            print(f"""
    {b.name}
    
    Life: {b.life}
                """)
            
            round += 1
            
            if round == 10:
                break

fight = Round()
player = Player()
dragon = Dragon()
name = None

print(f"Hello Player!!\n\nYou are welcome at this RPG created by Murilo Ruas, where you are a knight that fights agaist a scary dragon.\n\nFor we begin, firstly, what's your name?")

name = input(">")
player.name = name

print("\tCool!! So you are {}, aren't you?\n\nSo {}, I'll tell you a knight's story...".format(name, name))
print("\tA knight was on a deadly mission to kill a dragon that has destroyed the city. King Rodolfo has sent him out with no hope of victory, because who would really believe that a man could defeat a dragon? What's more, all the “strongest warriors” in the kingdom didn't accept the mission, because they thought it was impossible to complete such a ridiculous mission. They said that because they were afraid. But he was different, he accepted the deadly mission without a second thought, now there's no turning back. When he left the village with his horse and his weapons, the villagers called him \"crazy\"")
print("\tOn the way, he hears a roar from afar and smoke rising from the trees. He goes there and finds nothing but some burnt trees and the ground. He was about to leave, but out of nowhere he felt an absurd pressure coming from behind him, it was the dragon that seemed to be about 5 meters tall on 4 legs; and with a length of about 8 meters, it stared him in the eye ready to kill him. He froze and found himself in a dilemma: Run or Fight. What do you think he did?\n\nType 1 for Run or 2 for Fight:")

dilemma = int(input(">"))

if dilemma is 1: 
    #if dilemma == 1
    print("Yes, he runs. But his horse wasn't fast enough, because the dragon flies. The dragon breathes fire, what he did?\n\nType 1 for Give Up or 2 for Stay fighting:\n\n")

    choice = int(input(">"))

    if choice == 1:
        fight.start(player, dragon)

elif dilemma is 2:
    #if dilemma == 2
    print("He fightes agaist the dragon")