print("Let's practise everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\nnewlines and \t tabs")     #"\'" é aspas únicas ', \\ é barra \, \t é o tab e o bom e velho \n é o quebra-linha. 

poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""     #Variavel com o poema.

print("------------------")
print(poem)
print("------------------")

def secret_formula(started):    #A função usa started como parâmetro para fazer os cálculos abaixo.
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)   #Atribuição de novas variáveis para representar as outras que estão dentro da função.

print("With a starting point of: {}".format(start_point))   #Print da variavel start_point.
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")    #Print das variáveis com format.

start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)   #Essa "formula" armazena a função secret_formula usando start_point como parâmetro.

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))   #Ainda não sei que esse "*formula" serve.