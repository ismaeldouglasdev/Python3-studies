"""
Faça um programa que tenha uma função
chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
"""
print('<< Calculo do Terreno >>')


def area(a, b):
    r = a * b
    print(f'A área do terreno {a}x{b} é {r:.2f}m².')


x = float(input('Digite a altura do terreno (m): '))
z = float(input('Digite a largura do terreno (m): '))
area(x, z)
