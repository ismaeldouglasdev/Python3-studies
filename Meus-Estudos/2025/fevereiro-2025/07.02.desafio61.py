"""
aula 14: desafio 61
"""
"""
refaça o desafio 051, lendo
o primeiro termo e a razão
de uma PA. mostrando os 
10 primeiros termos da progressão
usando a estrutura while.
"""
print('Gerador de PA')
print('-=' * 10)
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = t
cont = 1
print('Os termos da PA são: ')
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
