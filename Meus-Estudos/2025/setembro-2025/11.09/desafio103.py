"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.

O programa deverá conseguir mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome, gols):
    print('-'*45)
    print('Ficha do Jogador:')
    print('-'*45)
    nome.capitalize()
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 0
    msg = f"O jogador {nome} fez {gols} gol(s) no campeonato."
    return msg


a, b = input('Nome do jogador: '), input('Quantidade de gols: ')
r = ficha(a, b)
print(r)
