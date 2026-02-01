"""
Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.
"""
jogador = dict()
gols = list()
t = 0
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = a = int(input('Quantas partidas o jogador jogou?: '))

print('Quantos gols ele fez em cada partida?')
for i in range(a):
    b = int(input(f'Partida {i+1}: '))
    t += b
    gols.append(b)
    jogador['gols'] = gols
print('-='*15)
print(f'O jogador {jogador["nome"]}, jogou {jogador["partidas"]} partidas.')
for i in range(a):
    print(f'=> Na partida {i+1}, fez {gols[i]} gols.')
print(f'Total de gols feitos durante o campeonato: {t}')
