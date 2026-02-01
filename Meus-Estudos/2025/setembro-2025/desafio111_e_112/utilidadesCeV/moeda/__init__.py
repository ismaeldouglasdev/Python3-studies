def aumentar(n, a, f=False):
    n += n * a/100
    if f:
        return f'{moeda(n)}'
    else:
        return n


def diminuir(n, r, f=False):
    n -= n * r/100
    if f:
        return f'{moeda(n)}'
    else:
        return n


def dobro(n, f=False):
    n = n*2
    if f:
        return f'{moeda(n)}'
    else:
        return n


def metade(n, f=False):
    n /= 2
    if f:
        return f'{moeda(n)}'
    else:
        return n


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, a, r):
    print('-'*50)
    print(f'\033[32m{"RESUMO DE VALOR":^50}\033[0m')
    print('-'*50)
    print(f'{"Preço Analisado:":<25}\033[34m{moeda(n):>15}\033[0m')
    print(f'{"Dobro do preço:":<25}\033[34m{dobro(n, True):>15}\033[0m')
    print(f'{"Metade do preço:":<25}\033[34m{metade(n, True):>15}\033[0m')
    print(f'{a}{"% de aumento do preço:":<23}\033[34m{aumentar(n, a, True):>15}\033[0m')
    print(f'{r}{"% de redução do preço:":<23}\033[34m{diminuir(n, r, True):>15}\033[0m')
    print('-'*50)
