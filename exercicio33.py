"""num = 0
numeros = []

while num < 10:
    print(f"A variável \"num\" vale {num}")
    numeros.append(num)
    print(numeros)

    num += 1

    print(f"Agora a variável \"num\" vale {num}")

print(f"Agora, a lista completa:\n {numeros}")"""

def enquanto_maior():
    a = input("Digite o primeiro valor:\n>")
    b = input("Agora finalmente, digite o segundo valor:\n>")

    if a > b:
        print(f"\"a\" vale {a}, e \"b\" vale {b}.")
        print(f"{a} é maior que {b}.")
        b = b + 1
        print(f"Agora, \"b\" vale {b}.")
    
    elif b < a:
        return enquanto_maior() 

print(enquanto_maior())