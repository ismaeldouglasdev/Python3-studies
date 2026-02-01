"""
Crie um módulo chamado moeda.py que tenha
as funções incorporadas aumentar(), diminuir()
dobro() e metade().

Faça também um programa que importe esse módulo
e use algumas dessas funções.
"""
from moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10% de {p} temos {aumentar(p)}')
print(f'Reduzindo 13% de {p} temos {diminuir(p)}')
