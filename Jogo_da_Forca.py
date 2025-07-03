import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system("clear")