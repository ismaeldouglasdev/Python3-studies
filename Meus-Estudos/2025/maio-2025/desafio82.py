"""
Crie um programa que vai ler vários números
e colocar em uma lista.

Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os
valores impares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""
a = list()
a_p = list()
a_i = list()
while True:
    try:
        b = int(input('Digite um número: '))
    except ValueError:
        print('Digite um número válido.')
        continue
    a.append(b)
    if b % 2 == 0:
        a_p.append(b)
    else:
        a_i.append(b)
    p = input('Quer continuar?[s/n] ')
    if p.lower() in ['nao', 'não', 'n']:
        break
print(f'Essa é a lista de todos os números: {a}')
print(f'Essa é a lista de todos os números pares: {a_p}')
print(f'E essa é a lista dos números ímpares: {a_i}')
