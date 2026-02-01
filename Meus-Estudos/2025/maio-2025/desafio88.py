"""
Faça um programa que ajude um jogador
da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 a 60
para cada jogo, cadastrando tudo em
uma lista composta.
"""
import random
import time

# Lista composta:
jogos = []
a = []

# Cabeçalho:
print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)

# Inputação de dados:
x = int(input('Quantos jogos você quer que eu sorteie? '))
print("-="*3, f' SORTEANDO {x} JOGOS ', "-="*3)

# Loop de impressão do produto final:
for i in range(x):
    a = [random.sample(range(0, 61), 6)]
    jogos.append(a)
    print(f'Jogo {i+1}: {a}')
    time.sleep(1.2)
print("-="*5, '< BOA SORTE! >', "-="*5)



