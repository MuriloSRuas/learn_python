from random import randint

cores = ['Azul', 'Branco', 'Preto', 'Amarelo', 'Rosa', 'Verde']
modelos = ['Sedan', 'Hot-Hatch', 'Jipe', 'Caminhonte', 'Esportivo']
marchas = [4, 5, 6, 7, 8]

print("Bem-vindo(a) ao criador de carros aleatórios, aqui temos cores, modelos e quantidade de marchas para vocẽ montar o seu carro:\n")
for color in range(0, len(cores)):
    print("Cor: ", cores[color])

print("\n")

for model in range(0, len(modelos)):
    print("Modelo: ", modelos[model])

print("\n")

for gear in range(0, len(marchas)):
    print("Marchas: ", marchas[gear])

rand_one = randint(0, 5)
rand_two = randint(0, 5)
rand_three = randint(0, 6)

print(f"Agora vamos juntas essas caracteristicas e montar um carro bem aleatório:\n O carro tem cor: {cores[rand_one]}.\n É de modelo: {modelos[rand_two]}.\n E tem {marchas[rand_three]} marchas.")
