"""
aula 13: laços de repetição: desafio 48
"""
"""
crie um programa que calcule a soma 
entre todos os números impares que 
são multiplos de três e que se encontram
no intervalo de 1 até 500.
"""
s = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print('A soma de todos os números foi {}'.format(s))
