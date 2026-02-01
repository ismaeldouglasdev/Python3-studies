""""
(desafio 63 já foi feito, apenas não está no pc.)
DESAFIO 64:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag)
"""
n = 0
q = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
    q += 1
print('Foram digitados {} números, e a soma deles resulta em: {}.'.format(q,s))
