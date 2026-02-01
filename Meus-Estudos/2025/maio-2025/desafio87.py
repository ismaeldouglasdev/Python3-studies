"""
Aprimore o desafio anterior,
mostrando no final:

a) a soma de todos os valores pares digitados.
b) a soma dos valores da terceira coluna.
c) o maior valor da segunda linha.
"""
# Criação da matriz:

matriz = [[], [], []]
a = b = c = p = s3 = ma = 0

# Loop para iteração dos valores da matriz:

for _ in range(0, 9):

    # Inputação de dados em cada coluna da matriz:

    v = int(input(f'Digite um valor para {[a , b]}: '))
    if c < 3:
        matriz[0].append(v)
        if c == 3 and v > ma:
            ma = v
    if c >= 3:
        matriz[1].append(v)
        if c == 4 and v > ma:
            ma = v
    if c >= 6:
        if c == 5 and v > ma:
            ma = v
        matriz[2].append(v)
        s3 += v
    # Processamento dos dados:

    if v % 2 == 0:
        p += v

    # Contador de posição de cada valor na matriz:

    c += 1
    b += 1
    if c >= 3 and b >= 3:
        a += 1
        b = 0

# Impressão da matriz:

print('-=' * 15)
print(f"""( {matriz[0][0]} )( {matriz[0][1]} )( {matriz[0][2]} )
( {matriz[1][0]} )( {matriz[1][1]} )( {matriz[1][2]} )
( {matriz[2][0]} )( {matriz[2][1]} )( {matriz[2][2]} )""")
print('-=' * 15)

print(f'A soma de todos os valores pares digitados, resulta em {p}.')
print(f'A soma dos valores da terceira coluna resulta em {s3}.')
print(f'O maior valor da segunda linha é {ma}.')