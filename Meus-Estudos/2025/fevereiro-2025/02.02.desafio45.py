"""
crie um programa que faça
o computador jogar jokenpô
com você.

desafio 45
"""
from random import choice
print('Vamos jogar jokenpô!')
possibilidades = ['pedra', 'papel', 'tesoura']
a = choice(possibilidades)
r = input('Escolha o que vai jogar: ').lower()
if r == 'pedra' and a == 'papel':
    print('Você jogou pedra, e eu papel, eu ganhei! ')
elif r == 'pedra' and a == 'pedra':
    print('Nós dois jogamos pedra! Deu empate!')
elif r == 'pedra' and a == 'tesoura':
    print('Você escolheu pedra, e eu tesoura, eu perdi, parabéns!')
elif r == 'tesoura' and a == 'papel':
    print('Você jogou tesoura, e eu papel, eu perdi! ')
elif r == 'tesoura' and a == 'tesoura':
    print('Nós dois jogamos tesoura! Deu empate!')
elif r == 'tesoura' and a == 'pedra':
    print('Você escolheu tesoura, e eu pedra, eu ganhei, parabéns pra mim!')
elif r == 'papel' and a == 'tesoura':
    print('Você jogou papel, e eu tesoura, eu ganhei! ')
elif r == 'papel' and a == 'papel':
    print('Nós dois jogamos papel! Deu empate! melhor de 3?')
elif r == 'papel' and a == 'pedra':
    print('Você escolheu papel, e eu pedra, ouch! eu perdi, parabéns!')
