"""
ex01
Tabuada de um número

Solicite ao usuário um número e
imprima a tabuada desse número de 1 a 10.
"""
#n = int(input('Insira um número: '))
#for num in range(0, 10):
#    print(f'{n} * {num} = {n * num}')

"""
ex02
Soma dos números pares

Calcule e imprima a 
soma de todos os números pares entre 1 e 100.
"""
"""
s = 0
for n in range(0, 101):
    if n % 2 == 0:
        s += n
print(f'A soma de todos os números pares de 0 a 100, resulta em {s}')
"""
"""
ex03
Média de notas

Peça ao usuário para digitar 5 notas e,
ao final, calcule e mostre a média dessas notas."""
"""print('Digite as cinco notas para calcular sua média.')
t = 0
for _ in range(0, 5):
    notas = float(input('Digite uma nota: '))
    t += notas
print(f'Sua média final é {t/5:.2f}.')"""
"""
ex04
Maior e menor valor

Leia 7 valores inteiros e, 
no final, mostre o maior e o menor valor digitado
"""
"""
ma = 0
me = 0
for n in range(0, 7):
    num = int(input('Digite um numero: '))
    if ma == 0:
        ma += num
    elif num > ma:
        ma = num
    if me == 0:
        me += num
    elif me > num:
        me = num
print(f'O maior número digitado {ma}, e o menor foi {me}')
"""