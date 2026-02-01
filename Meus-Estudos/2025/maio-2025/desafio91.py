"""
Crie um programa onde 4 jogadores
joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""
import random
from time import sleep

# Declaração das variáveis compostas:

r = dict()
n = ['Marcos', 'Maria', 'Lucas', 'Ana', 'Flávia', 'Marcelo', 'Nicolas']

print('=-'*15)
print('Os jogadores vão jogar os dados!')
print('=-'*15)

# Sorteando os jogadores e pontuações:

random.shuffle(n)
for i in range(0, 4):
    d = random.randint(1, 6)
    r[f'{n[i]}'] = d
    sleep(1.3)
    print(f'{n[i]}, tirou {d} no dado')
sleep(2)

# Ordenando o dicionário pelo valor
# (pontuação), do maior para o menor:

r_ordenado = sorted(r.items(), key=lambda item: item[1], reverse=True)
d_ordenado = dict(r_ordenado)

# Imprimindo a pontuação dos jogadores:
print('-='*15)
print('Ranking dos jogadores: ')
print('-='*15)
for i, (a, pontuacao) in enumerate(r_ordenado, start=1):
    if pontuacao != 1:
        print(f'{i}° lugar: {a} com {pontuacao} pontos.')
    else:
        print(f'{i}° lugar: {a} com {pontuacao} ponto.')
