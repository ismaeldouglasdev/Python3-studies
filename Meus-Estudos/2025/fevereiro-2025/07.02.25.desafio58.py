"""
aula 14: desafio 58
"""
"""
melhore o jogo do desafio 28 onde 
o computador vai "pensar" em um
número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar
até acertar, mostrando no final quantos 
palpites foram necessários para vencer.
"""
from random import randint
from time import sleep
p = 0
p1 = 0
n = randint(0, 10)
print('-=-' * 20)
print('Eu pensei em um número, duvido você adivinhar qual foi! hahaha')
print('-=-' * 20)
while p != n:
    p = int(input('Acho que o número é: '))
    if p == n:
        print('Você Acertou! Droga eu perdi >:(')
        if p1 == 0:
            print('Foi necessário apenas 1 palpite pra você adivinhar, você é um gênio!')
        else:
            print('Foram necessários {} palpites, para você adivinhar'.format(p1 + 1))
    else:
        p1 += 1
        print('Errou! tente novamente... ')
