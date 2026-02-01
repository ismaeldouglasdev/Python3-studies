"""
Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista.

no final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições
na lista.
"""
lista = []

# leitura dos 5 valores
for n in range(0, 5):
    lista.append(int(input('Insira um número: ')))

# inicializa maior e menor com o primeiro valor da lista
ma = lista[0]
me = lista[0]
# listas para armazenar as posições do maior e menor valor
p = [0]
w = [0]

# percorre a lista a partir da segunda posição
for pos in range(1, 5):
    valor = lista[pos]

    # verifica maior valor
    if valor > ma:
        ma = valor
        p = [pos]  # reseta a lista com a nova posição
    elif valor == ma:
        p.append(pos)  # adiciona posição igual ao maior

    # verifica menor valor
    if valor < me:
        me = valor
        w = [pos]  # reseta a lista com a nova posição
    elif valor == me:
        w.append(pos)  # adiciona posição igual ao menor

print(f'O maior valor digitado foi {ma} nas posições {p}')
print(f'E o menor valor digitado foi {me} nas posições {w}')