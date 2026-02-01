"""
Crie um programa que tenha uma tupla
com várias palavras (não usar acentos)
Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
"""
palavras = ('robo', 'arroz', 'cachorro', 'china',
            'pastel', 'balao', 'auditorio')
for palavra in palavras:
    print(f'\nPalavra: {palavra}')
    print('Vogais:', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')
