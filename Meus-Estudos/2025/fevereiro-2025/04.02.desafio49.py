"""
aula 13: laços de repetição: desafio 49
"""
"""
refaça o desafio 009, mostrando a tabuada
de um número que o usuário escolher, só que 
agora utilizando laço for.
"""
n = int(input('Insira um número: '))
for c in range(0,11):
    print('{} * {} = {}'.format(c, n, c*n))
