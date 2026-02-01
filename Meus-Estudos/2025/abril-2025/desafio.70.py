"""
Crie um programa que leia o nome e o preço
de vários produtos. o programa deverá perguntar
se o usuário vai continuar. no final, mostre:

a) qual é o  total gasto na compra.
b) quantos produtos custam mais de R$1000.
c) qual é o nome do produto mais barato.
"""
print('-='*10)
print("Sistema PDV")
print('-='*10)
n = ''
p = 0
t = 0
x = 0
pb = float('inf')
nb = ''
while True:
    n = input('Insira o nome do produto: ')
    p = float(input('Insira o preço do produto: '))
    t += p
    if p < pb:
        pb = p
        nb = n
    if p > 1000:
        x += 1
    while True:
        q = input('Deseja continuar?[s/n]:').lower()
        if q not in ('s', 'n'):
            print('Digite uma resposta válida!')
        else:
            break
    if q == 'n':
        break
print(f'O total gasto na compra foi de {t:.2f} reais.')
print(f'um total de {x} produtos custaram mais de R$1000.')
print(f'o nome do produto mais barato é: {nb}, com o preço de R${pb:.2f}')

