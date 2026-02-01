"""
Escrevaum programa que leia dois números
inteiros e compare-os, mostrando na tela
uma mensagem:

- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais
"""
print('Digite abaixo dois números inteiros: ')
n1 = input('Primeiro número: ')
n2 = input('Segundo número: ')
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')