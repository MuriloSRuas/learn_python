animais = ['Pato', 'Equidna', 'Tubarão', 'Cavalo', 'Cachorro', 'Canguru', 'Peixe-Dourado', 'Porco', 'Esquilo-Voador', 'Iguana']
habilidade = ['Cuspir fogo', 'Raio-Laser', 'Corpo mecânico', 'Super velocidade', 'Metamorfose', 'Criar hologramas', 'Ver o futuro', 'Causar terremotos']
estilo_de_luta = ['Kung-fu', 'Capoeira', 'Estilo selvagem', 'Master Cook-Fighter', 'Mágico', 'Sem estilo de luta', 'Palavras', 'Só na voadora']

print("Seja bem-vindo(a) ao criador misterioso de animais poderesos, digite um número e descubra qual combinação você vai conseguir.\n")
index1 = int(input("Digite um número de 1 à 10:\n>"))
index1 = index1 - 1

index2 = int(input("Digite um número de 1 à 8:\n>"))
index2 = index2 - 1

index3 = int(input("Digite um número de 1 à 8:\n>"))
index3 = index3 - 1

print(f"O resultado é: O seu animal é {animais[index1]}, ele tem a habilidade de {habilidade[index2]} e o seu estilo de luta é {estilo_de_luta[index3]}.")