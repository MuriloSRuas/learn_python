from sys import argv

script, nome_texto = argv

print("Vamos escrever!!")
print (f"Agora, nós vamos escrever alguma coisa usando o python no seu texto vazio {nome_texto}")
input("Vamo-nos?")

escrever = open(nome_texto, "+w")

print("Escreva alguma coisa no texto")
seu_texto = input(">")

escrever.write(seu_texto)
escrever.close()

print("Ficou assim:\n")
ler = open(nome_texto, "r")
print(ler.read())
ler.close()
