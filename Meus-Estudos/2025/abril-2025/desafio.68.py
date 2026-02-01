"""
faça um programa que jogue par ou ímpar
com o computador. o jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
import random
print("-="*10)
print("Jogo: Par ou Ímpar!")
print("-="*10)
pc = ''
c = 0
while True:
    r = input('\nInsira sua jogada (Par ou Impar!): ').lower()
    if r == 'par':
        pc = 'impar'
    if r == 'impar':
        pc = 'par'
    print(f'Ótimo! vou ficar com {pc} então')
    d = int(input('\nAgora insira a quantidade de dedos (0 à 10): '))
    dpc = random.randint(0, 10)
    print(f'Certo, eu escolhi {dpc} dedos.')
    soma = d + dpc
    print(f'A soma dos dedos foi {soma}')
    if soma % 2 == 0 and pc == 'par':
        print(f'O resultado foi par, eu venci! talvez na próxima amigo :)')
        if c == 1:
            print(f'\nVocê venceu apenas {c} vez.')
        else:
            print(f'\nVocê venceu {c} vezes consecutivas!')
        break
    if soma % 2 != 0 and pc == 'impar':
        print(f'O resultado foi impar, eu venci! talvez na próxima amigo :)')
        if c == 1:
            print(f'\nVocê venceu apenas {c} vez.')
        else:
            print(f'\nVocê venceu {c} vezes consecutivas!')
        break
    if soma % 2 == 0 and r == 'par':
        print(f'O resultado foi par e você venceu!')
        c += 1
    if soma % 2 != 0 and r == 'impar':
        print(f'O resultado foi impar e você venceu!')
        c += 1


