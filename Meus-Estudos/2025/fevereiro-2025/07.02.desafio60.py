"""
aula 14: desafio 60
"""
"""
faça um programa que leia um número
qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120
"""
n = int(input('Digite um número para ver seu fatorial: '))
r = 1
p = 1
if n == 0:
    print('O fatorial desse número é 1.')
elif n < 0:
    print('O fatorial não é definido para números negativos.')
elif n > 0:
    while p <= n:
        r *= p
        p += 1
    print('O fatorial de {}! é {}'.format(n, r))
