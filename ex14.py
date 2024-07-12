from sys import argv

yourComputer, you= argv

print(f"Hi {you}, I'm {yourComputer}, how are you?")
answer1= input()

print(f"Ok {you}, so, may I ask you anything? What's your favorite game?")
answer2= input()

print(f"Cool, and what do you like to watch?")
answer3= input()

print(f"{you}, I think you look like me, I like you, you like to play {answer2} and to watch {answer3}, it's good.")