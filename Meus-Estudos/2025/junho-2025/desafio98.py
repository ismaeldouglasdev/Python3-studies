"""
Faça um programa que tenha uma
função chamada contador(), que receba
três parâmetros: inicio, fim e passo
e realize a contagem.

Seu programa tem que realizar três
contagens através da função criada:

a) de 1 até 10, a cada 1.
B) de 10 até 0, a cada 2.
c) uma contagem personalizada.
"""
import time


def contador(inicio, fim, passo):
    print('-='*20)
    if fim < inicio:
        if passo > 0:
            print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
            for i in range(inicio, fim, -passo):
                print(i, end=' ')
                time.sleep(0.3)
            print(fim, end='')
            print(' FIM!')
        elif passo == 0:
            passo = 1
            print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
            for i in range(inicio, fim, -passo):
                print(i, end=' ')
                time.sleep(0.3)
            print(fim, end='')
            print(' FIM!')
        else:
            print(f'Contagem de {inicio} a {fim} de {abs(passo)} em {abs(passo)}:')
            for i in range(inicio, fim, passo):
                print(i, end=' ')
                time.sleep(0.3)
            print(fim, end='')
            print(' FIM!')
    else:
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
            time.sleep(0.3)
        print(' FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Contagem Personalizada:')
a = int(input('Insira o valor de inicio: '))
b = int(input('Insira o valor de fim: '))
c = int(input('Insira o valor de passo: '))
contador(a, b, c)

