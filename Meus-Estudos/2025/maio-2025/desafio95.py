"""
Aprimore o DESAFIO 093 para
que ele funcione com vários jogadores,
incluindo um sistema de visualização
de detalhes do aproveitamento
de cada jogador.
"""
import time
lista_jogadores = list()

while True:
    jogador = dict()
    lista_gols = list()
    t = 0
    print('-'*40)
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = a = int(input('Quantas partidas o jogador jogou?: '))
    for i in range(a):
        b = int(input(f'Partida {i+1}: '))
        t += b
        lista_gols.append(b)
        jogador['gols'] = lista_gols
    jogador['total_gols'] = t
    lista_jogadores.append(jogador.copy())
    print('Jogador criado:', jogador)
    i = input('Quer continuar?[S/N]: ')
    if i.lower() == 'n':
        break
print('-='*25)
print(f'{"cod:":<4} {"nome:":<9}{"gols:":<20}{"total"}')
print('---'*20)
for i, jogador in enumerate(lista_jogadores):
    print(f'{i:<4} {jogador["nome"]:<9}{str(jogador["gols"]):<20}{jogador["total_gols"]}')
print('---'*20)
while True:
    time.sleep(1.2)
    k = int(input('Mostrar dados de qual jogador?(cod): '))
    if k == 999:
        print('<< VOLTE SEMPRE! >>')
        break
    print('---' * 20)
    print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogadores[k]["nome"].upper()}:')
    for i, g in enumerate(lista_jogadores[k]['gols']):
        if g == 1:
            print(f'No jogo {i + 1} fez {g} gol.')
        else:
            print(f'No jogo {i+1} fez {g} gols.')
    print('---' * 20)


