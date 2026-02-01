"""
aula 14: desafio 59
"""
"""
crie um programa que leia dois valores
e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar 
a operação solicitada em cada caso.
"""
print('-=-' * 20)
print('Seja Bem-vindo(a)')
print('-=-' * 20)
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
n = 0
nv1 = 0
nv2 = 0
p = 0
while n != 5:
    print('\nO que você deseja fazer com esse(s) valor(es)?')
    print('Selecione uma das opções: ')
    n = int(input("""\n[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Digite: """))
    if n == 1 and nv1 == 0 and nv2 == 0:
        nv1 = v1 + v2
        print('\nA soma dos dois números resulta em: {}'.format(nv1))
    elif n == 1 and nv1 != 0 and nv2 != 0:
        nv1 = nv1 + nv2
        print('\nA soma dos dois valores é {}'.format(nv1))
    elif n == 1 and nv1 != 0 and nv2 == 0:
        print('Não há como somar se há apenas um valor.')
    elif n == 2 and nv1 == 0 and nv2 == 0:
        p = v1 * v2
        print('\nO produto dos dois valores é {}'.format(p))
    elif n == 2 and nv1 != 0 and nv2 == 0:
        print('Não há como multiplicar se há apenas um valor.')
    elif n == 2 and nv1 != 0 and nv2 != 0:
        p = nv1 * nv2
        print('\nO produto dos dois valores é {}'.format(p))
    elif n == 3 and nv1 == 0 and nv2 == 0 and p == 0:
        if v1 > v2:
            print('\nO maior número é o {}'.format(v1))
        else:
            print('\nO maior número é o {}'.format(v2))
    elif n == 3 and nv1 != 0 and nv2 == 0 and p == 0:
        print('Só há apenas um valor, o {} ele é o maior.'.format(nv1))
    elif n == 3 and nv1 != 0 and nv2 != 0 and p == 0:
        if nv1 > nv2:
            print('\nO maior número é o {}'.format(nv1))
        elif nv1 < nv2:
            print('\nO maior número é o {}'.format(nv2))
    elif n == 3 and nv1 == 0 and nv2 == 0 and p != 0:
        print('O maior número é {}'.format(p))
    elif n == 3 and nv1 != 0 and nv2 != 0 and p != 0:
        if nv1 > nv2 > p:
            print('O número {} é o maior'.format(nv1))
        elif nv2 > nv1 > p:
            print('O número {} é o maior'.format(nv2))
        elif p > nv1 > nv2:
            print('O produto {} é o maior número.'.format(p))
    elif n == 4:
        nv2 = int(input('Digite o novo  número: '))

