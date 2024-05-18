#!/usr/bin/env python3
'''
Uma simples tabuada de 1 a 10     
'''
import os 

__version__ = "0.0.1"
__author__ = "Henri Alves"
__license__ = "Unlicense"

# numeros = [1,2,3,4,5,6,7,8,9,10]

#numeros = range(1,11)
#print (numeros)
#print (type(numeros))

numeros = list(range(1,11))
print (numeros)
print (type(numeros))

# Iterable (percrriveis) <- significado

# para
for numero in numeros:
    print("====================")
    print("{:-^20}".format(f"Tabuado do: {numero}"))
    print("=" * 20)

    for outro in numeros:
        resultado = numero * outro
        # print(numero, " X ", outro , " = ", resultado )
        print("{:^20}".format(f"{numero} X {outro} = {resultado}"))
    print("=" * 20)

print('🍉') # copia do site de emoji 

