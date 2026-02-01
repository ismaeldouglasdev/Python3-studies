"""
Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar sort()).

No final, mostre a lista ordenada na tela.
"""
k = list()

for n in range(5):
    a = int(input('Digite um número: '))
    if len(k) == 0:
        pos = 0
        k.append(a)
        print(f'O número {a} foi adicionado na posição {pos} da lista.')
    else:
        pos = 0
        while pos < len(k) and k[pos] < a:
            pos += 1
        k.insert(pos, a)
        print(f'O número {a}, foi adicionado na posição {pos} da lista.')
print('Lista final:')
print(k)

