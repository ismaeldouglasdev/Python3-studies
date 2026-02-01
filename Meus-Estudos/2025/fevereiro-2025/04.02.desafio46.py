"""
aula 13: laços de repetição: desafio 46
"""
"""
Faça um programa que mostre na tela
uma contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com uma pausa 
de 1 segundo entre eles.
"""
from time import sleep
print('Queima de fogos em:')
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print('Feliz ano novo!!')