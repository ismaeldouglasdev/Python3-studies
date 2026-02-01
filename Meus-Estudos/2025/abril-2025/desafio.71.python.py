"""
crie um programa que simule o funcionamento
de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar
quantas cédulas de valor serão entregues.

obs: considere que o caixa possui cédulas
de R$50, R$20, R$10 e R$1.
"""
print("-="*10)
print("CAIXA ELETRÔNICO")
print("-="*10)
v = int(input("Qual será o valor a ser sacado? "))
n50 = v // 50
r = v % 50
n20 = r // 20
r = r % 20
n10 = r // 10
r = r % 10
n1 = r
print(f"Valor total {v}")
print(f"Serão {n50} notas de R$50")
print(f"{n20} notas de R$20")
print(f"{n10} notas de R$10 e {n1} notas de R$1.")

