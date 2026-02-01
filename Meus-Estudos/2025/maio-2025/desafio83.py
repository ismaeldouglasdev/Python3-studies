"""
Crie um programa onde o usuário digite
uma expressão qualquer que use parenteses
seu aplicativo deverá analisar se a expressão
passada está com os parenteses abertos e fechados
na ordem correta.
"""
a = list()
c = 0
b = input('Digite uma expressão: ')
a.append(b)
for i in a:
    for k in i:
        if '(' in k:
            c += 1
        elif ')' in k:
            c -= 1
if c == 0:
    print(f'A  expressão é válida!')
    print(f'Expressão digitada: {a}')
else:
    print('Expressão inválida, tente novamente.')
