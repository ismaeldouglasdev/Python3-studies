"""
aula 14: desafio 62
"""
"""
melhore o desafio 061, perguntando
para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.
"""
print('Gerador de PA')
print('-=' * 10)
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = t
p = 1
cont = 1
p1 = 0
print('Os termos da PA são: ')
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
    p1 += 1
# loop para mostrar mais termos
print('PAUSA', end='')
p = int(input('\nVocê quer ver mais quantos termos? '))
while p != 0:
    for _ in range (p):
        print('{} -> '.format(termo), end='')
        termo += r
        p1 += 1
    print('PAUSA', end='')
    p = int(input('\nVocê quer ver mais quantos termos? '))

print('Progressão finalizada com {} termos mostrados'.format(p1))
