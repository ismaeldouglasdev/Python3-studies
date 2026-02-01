"""
Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:

- se ele ainda vai se alistar aao serviço militar
- se é a hora de se alistar.
- se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
"""
print('Bem vindo ao site do alistamento!')
nasc = int(input('Insira seu ano de nascimento: '))
if nasc == 2007:
    print('''Essa é a hora de você se alistar! 
Você completa 18 anos esse ano, portanto, 
Procure a junta militar mais próxima.''')
elif nasc > 2007:
    print('''Você não está na idade de se alistar ainda,
faltam {} anos pra você precisar se alistar.'''.format(nasc - 2007))
elif nasc < 2007:
    print('''Já passou da hora de você se alistar,
Procure a junta militar mais próxima, você está {}
anos atrasado.'''.format(2007 - nasc))
else:
    print('Dados inválidos, tente novamente.')