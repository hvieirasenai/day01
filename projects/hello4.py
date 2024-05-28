#!/usr/bin/env python3
'''
Versão melhorada do Alo Mundo
    tenha a variavel LANG configurada em seu ambiente ex:
    export LANG=pt_BR
    Ou informe atraves do CLI argument "--lang=pt_BR" 
    ou o usuario terá de digitar :
    
    ### teste assim o programa :  
    # python hello4.py "--lang=  pt_BR" --count=10  --teste="   teste de duas"

'''
import os 
import sys

# print(sys.argv)
# print(f"{sys.argv=}")
# validação dos argumentos passados em linha de comando
arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError nos argumentos quando não há senal de =
    # print(f"{arg=}")
    # print(arg.split("="))
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    #print(key , value)
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key]= value
        
# Dunder = palavra em ingles que significa __ (duplo anderline) 
__version__ = "0.1.4"
__author__ = "Henri Alves"
__license__ = "Unlicense"


current_language = arguments["lang"]
if current_language is None:
    #TODO usar repetição 
    if "LANG" in os.environ:
        current_language = os.getenv("LANG") 
    else:
        current_language = input("Choose a language: ")
        
current_language = current_language[:5] 

# print(current_language)

msg = {
    "pt_BR": "Olá, Mundo!" ,          # Portugues BR
    "it_IT": "Ciao, Mondo!",          # Italiano
    "ru_RU": "Привет, мир !",         # Russo
    "fr_FR": "Bonjour le monde !" ,   # Francês 
    "de_DE": "Hallo Welt !",          # alemão
    "es_AR": "Hola Mundo !",          # Espanhol - Argentina
    "en_US": "Hello World !",         # Ingles
}

print((msg[current_language]+"\n") * int(arguments["count"]))
