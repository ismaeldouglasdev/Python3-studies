"""
aula 13: laços de repetição: desafio 51
"""
"""
desenvolva um programa que leia o primeiro termo 
e a razão de uma PA. no final, mostre os 10 primeiros
termos dessa progressão.
"""
t = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
d = t + (10 - 1) * r
print('Os termos da PA são:')
for c in range(t, d + r, r):
    print('{}'.format(c), end=' -> ')
print('Acabou!')