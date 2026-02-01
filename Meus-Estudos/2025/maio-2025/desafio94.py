"""
Crie um programa que leia nome, sexo e idade
de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista.
No final, mostre:

a) Quantas pessoas foram cadastradas
b) A média de idade do grupo.
c) Uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média.
"""


def linha():
    print('-='*15)


x = list()
mu = list()
a = list()
s = m = w = 0

while True:
    d = dict()
    d['nome'] = input('Digite o nome: ')
    d['sexo'] = input('Digite o sexo[M/F]: ')
    d['idade'] = int(input('Digite a idade: '))
    x.append(d.copy())

    s += d['idade']
    w += 1

    if d['sexo'].lower() == 'f':
        mu.append(d['nome'])

    p = input('Quer continuar?[S/N]')
    if p.lower() == 'n':
        break

m += s/w

linha()
print(f'Foram cadastradas {w} pessoas.')
linha()
print(f'A média de idade do grupo é {m:.2f}')
linha()
print(f'Mulheres: {mu}')
linha()
print('Pessoas com idade acima da média: ')

for d in x:
    if d['idade'] > m:
        a.append(d.items())
        print(f'nome = {d["nome"]}, sexo = {d["sexo"]}, idade = {d["idade"]}')


