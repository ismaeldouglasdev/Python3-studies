"""
desafio 066 - 07/04/25 - 15:20 - loja

crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. no final,
mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""
c = s = 0
while True:
    n = int(input('Insira um numero (999 para parar.): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'foram digitados {c} números e a soma deles resulta em {s}.')
