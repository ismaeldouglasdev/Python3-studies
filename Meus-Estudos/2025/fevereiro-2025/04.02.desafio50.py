"""
aula 13: laços de repetição: desafio 50
"""
"""
desenvolva um programa que leia 6 numeros 
inteiros, e mostre a soma apenas daqueles que forem pares
se o valor for impar ele será desconsiderado.
"""
s = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
     s += n
print('A soma dos números é {}'.format(s))
