from sys import argv    #importa os args(o que eu digito no terminal)

script, filename= argv  #Os dados que eu coleto no terminal estão aqui nessas variáveis

txt= open(filename) #Abre o arquivo

print(f"Here's your file {filename}")
print(txt.read())   #Imprime a leitura do arquivo

print("Type the filename again:")
file_again= input(">")  #Recebe o nome do arquivo, no meu caso o caminho

txt_again= open(file_again) #Abre o arquivo
                
print(txt_again.read()) #Imprime a leitura do arquivo novamente