from sys import argv    

script, arquivo_txt = argv

def imprimir_tudo(a):
    print(a.read())

def retroceder(a):
    a.seek(0)   #The comand seek() advance in bytes in text.

def imprimir_uma_linha(conta_linha, a):
    print(conta_linha, a.readline())

arquivo_atual = open(arquivo_txt)   #arquivo_atual is incremented in defs as "a".

print("Agora vamos printar o que tem dentro do arquivo:\n")
imprimir_tudo(arquivo_atual)

print("Agora vamos retroceder, que nem uma fita.")
retroceder(arquivo_atual)   

print("Agora vamos imprimir 3 linhas:\n")
linha_atual = 1

imprimir_uma_linha(linha_atual, arquivo_atual)  #In this three lines, I number them with the variable "linha_atual" in the begin of phrases.
linha_atual += 1  #This is same this: linha_atual = linha_atual + 1.
imprimir_uma_linha(linha_atual, arquivo_atual)
linha_atual += 1
imprimir_uma_linha(linha_atual, arquivo_atual)