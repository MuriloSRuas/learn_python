texto = "Olá eu sou {nome} , eu tenho {idade} anos".format(nome = "Murilo", idade= "17")

print(texto) 

#O .format é um formatador de variaveis para o tipo String, no código acima não é o caso, é só um jeito diferente de colocar uma variavel em uma frase.

"""
Isso:

    texto = "Olá eu sou {nome} , eu tenho {idade} anos".format(nome = "Murilo", idade= "17")

É a mesma coisa que isso:

nome= "Murilo"
idade= 17

print("Olá eu sou ", nome ,", eu tenho ", idade , " anos")

Que também é a mesma coisa que isso :

nome= "Murilo"
idade= 17

print(f"Olá eu sou {nome}, eu tenho {idade} anos")
"""

#Agora vou fazer o exercício 8

formatter= "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "You",
    "don't",
    "have",
    "enemies"
))

#Finalizado