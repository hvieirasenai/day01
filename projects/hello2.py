#!/usr/bin/env python3
'''
Helo word Multi Linguas

dependendo da lingua configurada no computador (ambiente) o programa exibirá
o Hello Word correspondente 

Como usar:
Tenha a variavel configurada no seu ambiente exemplo: LANG=pt_BR.UTF-8
Execução :
    python3 hello2.py
    ou 
    ./hello2.py
    
'''
import os 

# Dunder = palavra em ingles que significa __ (duplo anderline) 
__version__ = "0.0.1"
__author__ = "Henri Alves"
__license__ = "Unlicense"

# Este programa vai imprimir o famoso Hello Word na linguagem definida no ambeinte 

#if __name__ == "__main__":
#    print('Hello Word !')
# built-in (pre instalado dentro da linguagem)
# dois exemplos : variavel[:5]   assim pega os 5 primeiros caracteres 
# ou 
# variavel.split(".")  assim divide a variavel em duas 
"""
    dentro do python
    
    >>> import os
    >>> variavel = os.getenv("LANG")
    >>> variavel[:5]
    'pt_BR'
    >>> len(variavel)
    11
    >>> variavel.split(".")
    ['pt_BR', 'UTF-8']
    >>> 
    >>> 
"""


# snake_case  = tudo minusculo 
# current_language = os.getenv("LANG")[:5]
current_language = os.getenv("LANG", "en_US")[:5] 
# neste caso o segunto parametro é usado quando o objeto é nulo (ou seja quando não existir )
# a variavel de ambiente LANG setada no ambiente 

msg = 'Hello World !'

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "ru_RU":
    msg = "Привет, мир !"
elif current_language == "fr_FR": # Francês 
    msg = "Bonjour le monde !"
elif current_language == "de_DE": # alemão
    msg = "Hallo Welt !"
elif current_language == "es_AR":
    msg = "Hola Mundo !"


print(msg)



