"""
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços,
na sequência.

No final, mostre uma listagem de preços, organizando
os dados em forma tabular.
"""
p = ('Arroz', 23.50,
     'Leite', 9.80,
     'Pão', 5.60,
     'Batata', 8.90)
print('--'*21)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*21)
for pos in range(0, len(p)):
     if pos % 2 == 0:
          print(f'{p[pos]:.<35}',end='')
     else:
          print(f'R${p[pos]:>5.2f}')
print('--'*21)