"""
A confederação nacional de natação
precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo
com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: senior
- acima: master
"""
print('''Querido atleta, para saber sua categoria
informe seu ano de nascimento abaixo:''')
b = int(input('Ano de nascimento: '))
a = 2025 - b
if a <= 9:
    print('Sua categoria é Mirim.')
elif a > 9 and a <= 14:
    print('A sua categoria é Infantil.')
elif a > 14 and a <= 19:
    print('A sua categoria é Junior.')
elif a > 19 and a <= 20:
    print('A sua categoria é senior.')
else:
    print('A sua categoria é master.')
