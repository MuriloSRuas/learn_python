"""
from sys import argv

script, first, second, third= argv  #The "script" is this script, so it just was imported as "exercicio13.py"

print("Script is called:", script)
print("Your first variable is:", first)
print("Your second variable is", second)
print("Your third variable is:", third)

#In this exercise I had to type another thing, this "/bin/python3 /home/murilo/estudos/python/learn_python/exercicios_python/exercicio13.py" and the arguments. 
"""

from sys import argv

a, b, c, d, e, f, g= argv

print(f"""
-{a}
-{b}
-{c}
-{d}
-{e}
-{f}
-{g}""")

carroFavorito= input("Qual deles é o seu favorito?\n\t")
print(carroFavorito)

"""
a= argv
                    In this example I don't needed to type, because the first variable just was imported.
print(f"\n{a}")
"""