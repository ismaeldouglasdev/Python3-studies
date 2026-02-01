"""
Refaça o desafio 035 dos triângulos,
acrescentando o recurso de mostrar que tipo
de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
"""
a1 = int(input('Insira a primeira reta: '))
b2 = int(input('Insira a segunda reta: '))
c3 = int(input('Insira a terceira reta: '))
if a1 == b2 and a1 == c3:
    print('''Esse é um triângulo equilátero!
pois todos os seus lados são iguais.''')
elif a1 == b2 or a1 == c3:
    print('''Esse é um triangulo isósceles, 
pois ele tem pelo menos dois lados iguais!''')
elif a1 > b2 and a1 < c3 or a1 > c3 and a1 < b2:
    print('''Esse é um triangulo escaleno, 
pois todos os seus lados são diferentes.''')
else:
    print('Essas retas não podem formar um triângulo.')
