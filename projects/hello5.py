#!/usr/bin/env python3
'''
Versão melhorada do Alo Mundo
    tenha a variavel LANG configurada em seu ambiente ex:
    export LANG=pt_BR
    Ou informe atraves do CLI argument "--lang=pt_BR" 
    ou o usuario terá de digitar :
    
    ### teste assim o programa :  
    # python hello4.py "--lang=  pt_BR" --count=10  --teste="   teste de duas"

FAZENDO o TODO 

'''
# Dunder = palavra em ingles que significa __ (duplo anderline) 
__version__ = "0.1.5"
__author__ = "Henri Alves"
__license__ = "Unlicense"

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
    # Para acontecer o erro passe o parametro sem o sinal de = 
        # print(f"{arg=}")
        # print(arg.split("="))
    try:
        key, value = arg.split("=")
    except ValueError as e:
        print(f"[Error Code:100]{str(e)}")
        print("You need to use '=' ") 
        print(f"Uou passed {arg}")
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()
    
    print(key , value)
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        print(f"The options are: {arguments.keys()}")
        sys.exit()
    arguments[key]= value
        

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

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[Error] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(10) 

# message = msg.get(current_language, msg["en_US"])
    
print((message + "\n") * int(arguments["count"]))
