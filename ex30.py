pizzas = 42
motoboys = 50
clientes = 32

#If: É o primeiro condicional.
#
#Elif: É o segundo, só é executado quando o primeiro(if) não ter a sua condição satisfeita.
#
#Else: É o terceiro, quando nenhum dos de cima ficarem satisfeitos, else é executado.

if motoboys == 0:
    print("Vish, e agora? Quem vai entregar as pizzas?")

elif motoboys < pizzas:
    print("Temos poucos motoboys para muitas pizzas.")

elif motoboys > pizzas:
    print("Eles vão entregar rapidinho.")

if clientes > pizzas: 
    print("Ei!! Não tem pizza pra todo mundo.")

else:
    print("Pizzzzzzaaaaaaa!!")