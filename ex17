from sys import argv
from os.path import exists  #Aqui importamos a função "exists()"

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#Nós poderiamos fazer essas do=uas linhas em uma só, como?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")   #"len" é um função que mostra o tamanho do arquivo em bytes.

print(f"Does the output file exist? {exists(to_file)}") #'exists()' é um função para verificar se o arquivo existe. Ele retorna "true" ou "false".
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#Aqui nós copiamos o que estava em "from_file" e escrevemos em "to_file", isso só é possível porque lemos o primeiro arquivo com o '.read()'.
out_file = open(to_file, "w")   #Precisamos de criar a váriavel 'out_file' porque não podemos dar simplesmente um 'open()' sozinho, ele precisa estar dentro de uma variável.
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
