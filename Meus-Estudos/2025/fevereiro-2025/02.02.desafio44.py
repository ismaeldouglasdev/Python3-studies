"""
(desafio 44)
Elabore um programa que calcule o valor
a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.
"""
from time import sleep
prod = float(input('Qual o preço do produto? '))
print('Escolha sua forma de pagamento: ')
sleep(2)
print("""
[1] à vista/dinheiro/cheque (desconto de 10%)
[2] à vista no cartão (desconto de 5%)
[3] em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)
""")
r = int(input('Digite a opção desejada: '))
if r == 1:
    print('O valor a pagar fica: R${:.2f}!'.format(prod - (10/100 * prod)))
elif r == 2:
    print('O valor a pagar fica: R${:.2f}!'.format(prod - (5/100 * prod)))
elif r == 3:
    print('O valor a pagar fica: R${:.2f}!'.format(prod))
elif r == 4:
    print('O valor a pagar fica: R${:.2f}!'.format(prod + (20/100 * prod)))
