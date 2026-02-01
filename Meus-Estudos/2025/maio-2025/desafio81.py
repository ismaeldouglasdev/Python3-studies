"""
Crie um programa que vai ler vários números e colocar
em uma lista.

Depois disso, mostre:

a) quantos números foram digitados.
b) a lista de valores ordenada de forma decrescente.
c) se o valor 5 foi digitado e está ou não na lista.
"""
n = 0
x = 0
a = list()
while True:
    try:
        b = int(input('Digite um número: '))
    except ValueError:
        print('Digite um número válido.')
        continue
    a.append(b)
    a.sort(reverse=True)
    if b == 5:
        x = 1
    q = input('Quer continuar?[s/n]: ')
    if q.lower() in ['não', 'n', 'nao']:
        break
print(f'Foram digitados {len(a)} números')
print(f'Lista dos números:{a}')

if x == 1:
    pos5 = [i for i, x in enumerate(a) if x == 5]
    print(f'O valor 5 foi digitado e está na lista nas posições {pos5}')
else:
    print(f'O valor 5 não foi digitado.')
