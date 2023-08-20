types_of_people = 10    #Declarei a variável do tipo inteiro
x = f"Aqueles são os {types_of_people} tipos de pessoas"    #Declarei uma variavel do tipo string com o format

binary = "binário"   #declarei outra variavel do tipo inteiro
do_not = "não"
y = f"Aqueles que sabem {binary} e aqueles que {do_not} sabem"

print (x)
print (y)

print (f"Eu disse : {x}")
print (f"Eu também disse : '{y}'")

hilarious = False
joke_evaluation = "Aquela piada é muito engraçada ?! {}"

print (joke_evaluation.format(hilarious))

w = "Isso é o lado esquerdo de..."
e = "uma string com um lado direito."

print (w + e)