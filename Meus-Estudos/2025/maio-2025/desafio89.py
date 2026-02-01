"""
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo média de cada um e permita
que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
# Criação da lista composta:

alunos = [[], [], [], []]

# Declaração de variáveis:

x = m = 0

# Loop de inputação de dados:

while True:

    # Inputação de dados:

    nome = input('Insira o nome: ')
    alunos[0].append(nome)
    nota1 = int(input('Insira a primeira nota: '))
    alunos[1].append(nota1)
    nota2 = int(input('Insira a segunda nota: '))
    alunos[2].append(nota2)

    # Contador de alunos:
    c = len(alunos[0])

    # Processamento de média:

    m = (nota1 + nota2) / 2
    alunos[3].append(m)

    # Verificação de condição:

    p = input('Deseja continuar cadastrando alunos? ')
    if p.lower() in ['n', 'nao', 'não']:
        break


# Impressão dos dados:

print(f'-=' * 20)
print(f'N°:  NOME:        MÉDIA:')
print('-' * 30)
for i in range(c):
    nome = alunos[0][i]
    nota1 = alunos[1][i]
    nota2 = alunos[2][i]
    media = alunos[3][i]

    print(f'{i + 1}. {nome}     {media}')

# Continuação da inputação de dados:
while True:

    x = int(input('Mostrar notas de qual aluno?[-1 Interrompe]: '))

    # Processamento das variáveis:

    nome = alunos[0][x - 1]
    nota1 = alunos[1][x - 1]
    nota2 = alunos[2][x - 1]

    # Interrupção do looping:

    if x == -1:
        break

    # Impressão dos dados:

    print(f'Notas de {nome} são {nota1, nota2}')
