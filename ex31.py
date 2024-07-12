#Menu do jogo
from random import randint

print("""
Seja bem-vindo ao RPG dos séculos, nesse jogão aqui você vai viver aventuras insanas.
Aqui você é um herói e o seu objetivo é salvar uma princesa que foi sequestrada por um bruxo maligno.
      
Digite o seu nome, herói:
    """)

nome = input(">")

#O jogo

print(f"OK {nome}, a sua aventura está prestes a começar...")
print(f"""
Você está caminhando pela floresta procurando frutas e lenha, até que uma criatura surge atrás do arbusto para atacar o seu braço com os seus dentes.
      
Você escolhe Esquiva(1) ou Defesa(2)?
      """)

escolha = input(">")

"""if dado < 10:
    #bla bla bla

elif dado == 10:
    #bla bla bla

else: 
    #bla bla bla"""

dado = randint(1,20)

if escolha == "1":
    print(dado)

    if dado < 10:
        print("Você tentou esquivar, mas foi mordido pela criatura.")
    
    elif dado == 10:
        print("Você esquivou perfeitamente.")

    else:
        print("Você esquivou e ainda o jogou para longe, causando -1 de dano nele.")

if escolha == "2":
    print(dado)

    if dado < 10:
        print("A mordida foi forte demais para você defender bem, você perdeu -5 de vida.")
    
    elif dado == 10:
        print("Defendeu bem. Isso fez a criatura aumentar a distância e ficar mais cauteloso")
    
    else:
        print("Defendeu tão bem que você criou uma abertura para contra-atacar, você contra-ataca? Sim(1) ou Não(2)")
        escolha_A = input()

        if escolha_A == "1":
            print(dado)

            if dado < 10:
                print("Você contra-atacou, mas a criatura repeliu o seu ataque e desta vez ela mordeu a sua perna esquerda, tirando -5 de vida.")

            elif dado == 10:
                print("Você acertou um golpe nele, que tirou -1 de vida dele. Mas ele ainda está de pé.")

            else: 
                print("Você acertou um golpe forte nele, que tirou -5 de vida. Ele fica caído no chão.")

print(f"""

Vocês estão se encarando, mas de repente a criatura escuta alguma coisa e foge adentro da mata. Você olha para trás e aparece alguem com um rifle e um chapéu.

E ele fala:

-Poxa vida, onde será que aquele Caçador Noturno foi?

Ele te vê, te cumprimenta e pergunta:

-Você é {nome} certo? Você por acaso viu uma criatura grande, peluda e com dentes de sabre? Se viu, pode me dizer para onde ela foi? 

Você pensa um pouco...
      
CONTINUA...
""")

#Fim