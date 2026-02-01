"""
desafio 79
05/24/2025 - 11:37am - saturday
"""

"""
Crie um programa onde o usuário possa
digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro,
ele não será adicionado, no final, serão exibidos
todos os valores únicos, em ordem crescente.
"""
n = list()
while True:
    a = (int(input('Digite quantos números quiser: ')))
    if a not in n:
        n.append(a)
    else:
        print('número duplicado! não será adicionado.')
    p = input('Deseja continuar? ').strip().lower()
    if p in ['nao', 'não', 'n']:
        break
n.sort()
print('números digitados:', n)
