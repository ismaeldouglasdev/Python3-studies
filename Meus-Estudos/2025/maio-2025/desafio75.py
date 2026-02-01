"""
Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla, no final,
mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os numeros pares.
"""
n = int(input('Insira o primeiro numero: '))
r = int(input('Insira o segundo: '))
f = int(input('Insira o terceiro: '))
g = int(input('Insira o quarto: '))
t = (n, r, f, g)
print(f'Você digitou os valores {t}')
np = 3
try:
    p = t.index(np)
    print(f'O número {np} foi encontrado na posição {p + 1}')
except ValueError:
    print(f'Não foi encontrado nenhum número 3.')
print(f'O numero 9 apareceu {t.count(9)} vezes')

print(f'Os números pares foram: ', end='')
for numero in t:
    if numero % 2 == 0:
        print(numero, end=' ')