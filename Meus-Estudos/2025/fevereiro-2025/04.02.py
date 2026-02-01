"""
aula 13: laços de repetição
"""
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))