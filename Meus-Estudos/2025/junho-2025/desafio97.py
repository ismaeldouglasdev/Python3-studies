"""
Faça um programa que tenha
uma função chamada escreva(),
que receba um texto qualquer
como parâmetro e mostre uma mensagem
com tamanho adaptável.

Ex:
escreva(Olá, Mundo!)

Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""


def escreva(f):
    print('-'*len(f))
    print(f)
    print('-'*len(f))


escreva('Arroz')
escreva('Baiacu do Pacífico')
escreva('Olá, Mundo!')
