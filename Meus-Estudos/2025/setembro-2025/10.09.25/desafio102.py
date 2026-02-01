"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será
um valor lógico (opcional), indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n=1, show=True):
    """
    — > Calcula o valor fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não o processo do cálculo.
    :return: O valor fatorial de um número n.
    """
    print('-' * 30)
    if show is True:
        c = 1
        for num in range(n, 0, -1):
            c *= num
            if num != 1:
                print(f'{num}', end=' x ')
            else:
                print(f'{num} =', c)
        print('-' * 30)
        return c
    else:
        c = 1
        for num in range(n, 0, -1):
            c *= num
        print('-' * 30)
        return c


print('-' * 30)
a = int(input('Insira um número: '))
print(f'O fatorial de {a} é {fatorial(a)}!')
print('-' * 30)
