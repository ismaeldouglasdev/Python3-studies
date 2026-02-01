"""
Faça um programa que tenha
uma função chamada maior(),
que receba vários parâmetros
com valores inteiros.

Seu programa tem que analisar
todos os valores e dizer
qual deles é o maior.
"""
import time


def maior(*num):
    m = 0
    print('-='*20)
    for n in num:
        if n > m:
            m = n
    print('Analisando os valores passados', end='')
    for p in range(3):
        time.sleep(0.3)
        print('.', end='')
    time.sleep(1.2)
    print('')
    for n in num:
        print(n, end=', ')
        time.sleep(0.3)
    if len(num) > 1:
        print(f'Foram informados {len(num)} valores ao todo.')
    elif len(num) == 1:
        print(f'Foi informado {len(num)} valor ao todo.')
    print(f'O maior valor informado é {m}.')


maior(1, 4, 5)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
