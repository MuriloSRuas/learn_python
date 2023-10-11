print("Olá, bem-vindo ao copiador de códigos!!")
print("Vc quer copiar algum texto?")
input()

print("Qual arquivo você quer copiar e para qual você quer passar o texto?")
file1 = input()
file2 = input()

no_file1 = open(file1)
textoF1 = no_file1.read()

no_file2= open(file2 , "+w")
no_file2.truncate()
no_file2.write(textoF1)
no_file2.close()

print("Tudo certo, ficou assim:")
abrirF2 = open(file2 , "r")
print("\n", abrirF2.read())

no_file1.close()
no_file2.close()