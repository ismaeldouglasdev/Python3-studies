"""
Faça um programa que leia nome e peso
de várias pessoas, guardando tudo em uma lista.
No final, mostre:

a) quantas pessoas foram cadastradas.
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
"""
nome = []
peso = []
x = ma = me = 0
ma_p = []
me_p = []
while True:

    # Inputar dados:

    # Testar se o nome é valido
    while True:
        try:
            a = str(input('Nome: '))
        except ValueError:
            print('Insira um nome válido!')
            continue
        nome.append(a)
        break
    # Testar se o peso é valido
    while True:
        try:
            b = int(input('Peso: '))
        except ValueError:
            print('Insira um peso válido!')
            continue
        peso.append(b)
        break
    x += 1

    # Verificar quais pessoas são as mais pesadas:
    if b == ma:
        ma_p.append(a)
    elif ma == 0:
        ma = b
        ma_p.append(a)
    elif b > ma:
        ma = b
        ma_p.clear()
        ma_p.append(a)

    # Verificar quais pessoas são as mais leves:
    if b == me:
        me_p.append(a)
    elif me == 0:
        me = b
        me_p.append(a)
    if b < me:
        me = b
        me_p.clear()
        me_p.append(a)

    # Verificar se o usuário quer continuar ou não:
    p = input('Quer continuar?[S/N] ')
    if p.lower() in ['n', 'nao', 'não']:
        break
    else:
        continue

print('-='*15)
print(f'Ao todo, você cadastrou {x} pessoas.')
print(f'O maior peso foi de {ma}kg. Peso de {ma_p[0:]}')
print(f'O menor peso foi de {me}kg. Peso de {me_p[0:]}')
