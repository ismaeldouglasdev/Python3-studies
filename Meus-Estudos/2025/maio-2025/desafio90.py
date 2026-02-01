"""
Desafio 90:
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""
# Declaração de dicionário e inputação de dados:

aluno = dict()
s = ''
aluno['nome'] = nome = str(input('Digite o nome: '))
aluno['media'] = media = float(input('Digite a média do aluno: '))

# Verificando condicional:

if media > 7:
    s = 'aprovado'
else:
    s = 'reprovado'
aluno['situacao'] = s

# Imprimindo o conteúdo:
print(f'O aluno {aluno["nome"]} está com a média {aluno["media"]} \nE foi {aluno["situacao"]}')
