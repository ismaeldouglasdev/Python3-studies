"""
aula 13: laços de repetição: desafio 53
"""
"""
crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando
os espaços.
(feito com perplexity)
"""
import re
p = input('Insira a palavra/frase: ')
p = re.sub(r"[^\w]", "", p.lower())
if p == p[::-1]:
    print('É um palindromo!')
else:
    print('Não é um palindromo.')"""

