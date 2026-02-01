"""
Crie um programa que crie uma matriz de
dimensão 3x3 e preencha com valores
lidos pelo teclado.
0 ( )( )( )
1 ( )( )( )
2 ( )( )( )
   0  1  2
No final, mostre a matriz na tela, com
a formatação correta.
"""

# Criação da matriz:
matriz = [[], [], []]

a = b = c = 0

# Loop para iteração dos valores da matriz

for _ in range(0, 9):

    # Inputação de dados em cada coluna da matriz

    v = int(input(f'Digite um valor para {[a , b]}: '))
    if c < 3:
        matriz[0].append(v)
    if c >= 3:
        matriz[1].append(v)
    if c >= 6:
        matriz[2].append(v)

    # Contador de posição de cada valor na matriz

    c += 1
    b += 1
    if c >= 3 and b >= 3:
        a += 1
        b = 0

# Impressão da matriz
print('-=' * 15)
print(f"""( {matriz[0][0]} )( {matriz[0][1]} )( {matriz[0][2]} )
( {matriz[1][0]} )( {matriz[1][1]} )( {matriz[1][2]} )
( {matriz[2][0]} )( {matriz[2][1]} )( {matriz[2][2]} )""")

