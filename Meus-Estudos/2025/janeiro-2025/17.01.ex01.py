"""Escreva um programa para aprovar
o empréstimo bancário para compra de uma
casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos
anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou
então o empréstimo será negado."""

print('Verifique abaixo, se você é elegível '
      'a adquirir o empréstimo para comprar a casa!')
valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))
v_prestacao = valor_casa/anos
if v_prestacao > (30/100) * salario:
    print('Empréstimo negado.')
else:
    print('Você é realmente elegível a esse empréstimo!')
