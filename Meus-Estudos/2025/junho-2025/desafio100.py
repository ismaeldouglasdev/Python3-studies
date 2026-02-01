"""
Faça um programa que tenha uma lista
chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai
mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
"""
import random
import time
numeros = list()


def sorteia(x):
    """
    - Sorteia X números e os coloca
    na lista numeros.
    :param x: Quantos valores serão sorteados
    :return: Sem retorno
    Função criada por Ismael Douglas
    """
    for _ in range(x):
        a = random.randint(0, 20)
        numeros.append(a)
    print(f'Sorteando valores da lista:')
    for q in numeros:
        print(q, end=', ')
        time.sleep(0.4)
    print('')


def soma_par(lista):
    print('-='*20)
    a = 0
    for n in lista:
        if n % 2 == 0:
            a += n
    time.sleep(1)
    print(f'A soma de todos os valores PARES \nde {lista} é {a}.')


sorteia(5)
soma_par(numeros)
help(sorteia)