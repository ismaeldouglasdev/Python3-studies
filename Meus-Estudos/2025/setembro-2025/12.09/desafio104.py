"""
Crie um programa que tenha a função leiaint(),
que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.

Ex:
n = leiaint('Digite um n')
"""


def leiaint(a):
    while True:
        try:
            v = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print("\033[31mERRO! digite um número válido\033[m")
    return v


# Programa principal
n = leiaint('')
print(f"\033[32mVocê acabou de digitar: {n}\033[m")
