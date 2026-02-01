"""
Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla.

depois disso, mostre a listagem de números
gerados e também indique o menor e o maior
valor que estão na tupla.
"""
from random import randint
n = tuple(randint(0, 100) for _ in range(5))
print('Números gerados: ', n)
print('Maior valor: ', max(n))
print('Menor valor: ', min(n))
