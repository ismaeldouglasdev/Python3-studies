"""
Reescreva a função leiaint() que fizemos
no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
"""


def leiaint(a):
    while True:
        try:
            v = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print("\033[31mERRO: Por favor, digite um número inteiro válido\033[m")
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            v = 0
            break
    return v


def leiafloat(a):
    while True:
        try:
            v = float(input('Digite um número real: '))
            break
        except ValueError:
            print('\033[31mErro: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            v = 0
            break
    return v


# Programa principal
n = leiaint('')
x = leiafloat('')
print(f"\033[32mO valor inteiro digitado foi {n} e o real foi {x}\033[m")
