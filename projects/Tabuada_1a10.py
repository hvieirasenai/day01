#!/usr/bin/env python3
'''
    Uma tabuada de 1 a 10
    com varios comandos      
'''
import os 

__version__ = "0.0.2"
__author__ = "Henri Alves"
__license__ = "Unlicense"

template = "{bloco01}"
# numeros = [1,2,3,4,5,6,7,8,9,10]

numeros = list(range(1,11))
print (numeros)
print (type(numeros))

# Iterable (percrriveis) <- significado

# para
for n1 in numeros:
    bloco01 = ""
    bloco01 += "====================\n"
    bloco01 += ("{:-^19}".format(f"Tabuado do: {n1} \U0001F43C")+"\n")
    bloco01 += "====================\n"

    for n2 in numeros:
        resultado = n1 * n2
        bloco01 += ("{:^19}".format(f"{n1} X {n2} = {resultado} \N{Basketball and Hoop}")+"\n")
    print(template.format(bloco01=bloco01))

print('🍉') # copia do site de emoji 

