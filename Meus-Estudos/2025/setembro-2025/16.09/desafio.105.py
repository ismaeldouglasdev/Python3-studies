"""
Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornando
um dicionário com as seguintes informações:

- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação (opcional)

adicione também as docstrings da função
"""


def notas(*a, sit=True):
    """
    Função para processar notas de alunos.
    :param a: Uma quantidade variável de notas dos alunos.
    :param sit: Definição da situação (Opcional)
    :return: Retorno dos dados processados das notas dos alunos.
    """
    # Declaração das variáveis:
    a, b, c, x, situacao = [*a], max(*a), min(*a), 0, 'Situação: Indefinida'
    # Cálculo da média:
    for n in [*a]:
        x += n
    m = x/len(a)
    # Situação:
    if sit:
        if m < 6:
            situacao = "Situação: RUIM"
        elif 6 <= m < 7:
            situacao = "Situação: RAZOÁVEL"
        else:
            situacao = "Situação: BOA"
    # Declaração dos resultados:
    e, f, g, m = (f'Quantidade de notas: {len(a)}', f'Maior nota: {b}', f'Menor nota: {c}', f'Média das notas: {m:.2f}')
    return e, f, g, m, situacao


# Programa principal
s = notas(4, 6.5, 6, 5, 7)
print(s)
