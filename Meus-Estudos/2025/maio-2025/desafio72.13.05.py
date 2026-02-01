"""
Crie um programa que tenha uma tupla
totalmente preenchida com uma contagem
por extensão, de zero até vinte.

seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
"""
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
n = ''
while n not in numeros:
    n = int(input('Digite um número de 0 a 20: '))
    if n > 20:
        print('Tente novamente. ', end='')
    if n < 0:
        print('Tente novamente. ', end='')
    if n <= 20 and n >= 0:
        print(f'O número digitado foi {numeros[n]}.')
    p = input('Você quer continuar? ')
    if p in 'nãonaonNãoNao':
        break
