"""
faça um programa que mostre a tabuada de
varios numeros, um de cada vez, para cada valor
digitado pelo usuario, o programa será interrompido
quando o número solicitado for negativo.
"""
i = 0
print('-='*10)
print('Gerador de Tabuadas!')
print('-='*10)
while True:
    n = int(input('Digite o número desejado: '))
    if n < 0:
        break
    while i != 11:
        print(f'{n} * {i} = {n * i}')
        i += 1
    i -= 11
