"""
Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final
de acordo com a média atingida:

- média abaixo de 5.0:
reprovado

- média entre 5.0 e 6.9:
recuperação

- média 7.0 ou superior:
aprovado
"""
nome = input('Digite o nome do aluno: ')
n0 = float(input('Digite a nota de história: '))
n1 = float(input('Digite a nota de geografia: '))
m = (n0 + n1)/2
if m <= 5.0:
    print('Aluno(a) {} Reprovado(a), a sua média foi {}.'.format(nome, m))
elif m > 5.0 and m < 6.9:
    print('Aluno(a) {} está de recuperação, a sua média foi {}'.format(nome, m))
elif m > 7.0:
    print('Parabéns! seu aluno(a) {} está aprovado(a)! sua média foi {}!'.format(nome, m))
