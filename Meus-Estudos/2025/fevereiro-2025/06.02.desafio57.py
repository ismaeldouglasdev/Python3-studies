"""
aula 14: desafio 57
"""
"""
faça um programa que leia
o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'.
Caso esteja errado, peça digitação novamente
até ter um valor correto.
"""
s = ''
while s != 'M' or s == 'F':
    s = input('Digite seu sexo: ')
    if s == 'M' or s == 'F':
        print('Cadastro realizado com sucesso!')
    else:
        print('Valor inválido, digite novamente (M ou F)')