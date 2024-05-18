#!/usr/bin/env python3
'''
Escreve o nome mais bonito em BYTES Unicode UTF-8
nome = 'Henri'
nome_bytes = bytes(nome, "utf-8")
nome_bytes     
nome_list = list(bytes(nome, "utf-8"))
nome_list
[72, 101, 110, 114, 105]
'''
import os 

__version__ = "0.0.1"
__author__ = "Henri Alves"
__license__ = "Unlicense"

numeros = [72, 101, 110, 114, 105]
print (numeros)
print (type(numeros))

print("=========================")
print("Escrevendo o Nome-> ", numeros)
print("-------------------------")

for numero in numeros:
    print(chr(numero), end='')
print()
print("-" * 24)

