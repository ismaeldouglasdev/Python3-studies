"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO
nas eleições.
"""


def voto(a):
    from datetime import date
    print('-'*40)
    x = date.today().year - a
    if x < 16:
        return f'Já que sua idade é {x}, você ainda não tem idade pra votar! NEGADO!'
    elif 16 <= x < 18 or x >= 65:
        return f'Já que sua idade é {x}, o seu voto é OPCIONAL!'
    else:
        return f'Já que sua idade é {x}, O seu voto é OBRIGATORIO!'


# Programa principal
b = int(input('Insira seu ano de nascimento: '))
print(voto(b))
