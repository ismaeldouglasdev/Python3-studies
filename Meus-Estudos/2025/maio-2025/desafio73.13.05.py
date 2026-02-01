"""
Crie uma tupla preenchida com os 20 primeiros
colocados na tabela do campeonato brasileiro
de futebol, na ordem de colocação. Depois
mostre:

a) Apenas os 5 primeiros colocados.
b) os últimos 4 colocados da tabela.
c) uma lista com os times em ordem alfabética.
d) em que posição na tabela está o time do Internacional.
"""
times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino',
         'Ceará', 'Bahia', 'Fluminense', 'Corinthians', 'Atlético-MG',
         'Botafogo', 'São Paulo', 'Mirassol', 'Vasco', 'Fortaleza',
         'Internacional', 'Vitória', 'Grêmio', 'Juventude', 'Santos', 'Sport')
print('Os cinco primeiro colocados: ')
print('-='*20)
print(times[0:5])
print('-='*20)
print('Os últimos quatro colocados da tabela: ')
print('-='*20)
print(times[16:])
print('-='*20)
print('Em ordem alfabética: ')
print('-='*20)
print(sorted(times))
print('-='*20)
print(f'O time Internacional está na posição {times.index("Internacional")+1}°')