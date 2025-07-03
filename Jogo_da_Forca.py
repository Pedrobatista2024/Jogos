import random
from os import system, name


def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system("clear")

def game():
    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo')

    palavras = ['banana','abacate','uva','morango','laranja']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []