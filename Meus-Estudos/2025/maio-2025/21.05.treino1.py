"""
Escreva um programa em Python que utilize um laço for
para imprimir todos os números pares entre 0 e 20 (inclusive),
 um em cada linha.
"""
for numero in range(0, 21, 2):
    if numero % 2 == 0:
        print(numero)