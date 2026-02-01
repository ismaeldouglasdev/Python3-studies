"""
Faça um mini-sistema que utilize o interactive help
do python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará.

OBS: use cores
"""
from colorama import init, Back, Fore
from time import sleep
import io
import sys

init(autoreset=True)


def sistema():
    while True:
        print(Back.GREEN + Fore.BLACK + '~'*40)
        print(Back.GREEN + Fore.BLACK + 'SISTEMA DE AJUDA PyHELP'.center(40))
        print(Back.GREEN + Fore.BLACK + '~'*40)
        print(Back.BLUE + Fore.BLACK + '~' * 40)
        f = input(Back.BLUE + Fore.BLACK + 'Função ou Biblioteca > '.center(35))
        print(Back.BLUE + Fore.BLACK + '~' * 40)
        if f.upper() == 'FIM':
            print(Back.RED + Fore.BLACK + '~' * 40)
            print(Back.RED + Fore.BLACK + 'ATÉ LOGO!'.center(40))
            print(Back.RED + Fore.BLACK + '~' * 40)
            break

        print(Back.MAGENTA + Fore.BLACK + f"Acessando o manual do comando '{f}'".center(40))
        sleep(1)

        # Salvar a saída padrão atual (a tela)
        old_stdout = sys.stdout

        # Criar uma "caixa" para capturar texto (uma espécie de arquivo em memória)
        mystdout = io.StringIO()

        # Redirecionar a saída padrão para nossa caixa/memória
        sys.stdout = mystdout

        help(f)

        # Restaurar a saída padrão para a tela
        sys.stdout = old_stdout

        # Pegar o conteúdo capturado como string
        help_text = mystdout.getvalue()

        # Mostrar o texto capturado
        print(Back.WHITE + Fore.BLACK + help_text)


# Programa Principal
sistema()
