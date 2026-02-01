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
    print(f'{"RESUMO DE VALOR":^50}')
    print('-'*50)
    print(f'{"Preço Analisado:":<25}{n:>15.2f}')
    print(f'{"Dobro do preço:":<25}{dobro(n, True):>15}')
    print(f'{"Metade do preço:":<25}{metade(n, True):>15}')
    print(f'{a}{"% de aumento do preço:":<23}{aumentar(n, a, True):>15}')
    print(f'{r}{"% de redução do preço:":<23}{diminuir(n, r, True):>15}')
    print('-'*50)
