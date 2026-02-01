"""
aula 13: laços de repetição: desafio 55
"""
"""
crie um programa que leia o peso
de cinco pessoas, no final, mostre
qual foi o meior e menor peso lidos.
"""
man = 0
men = 10**10
for i in range(1, 5+1):
    p = float(input('Insira o peso: '))
    if p > man:
        man = p
    if p < men:
        men = p
print('O maior peso foi {} e o menor peso foi {}'.format(man, men))

