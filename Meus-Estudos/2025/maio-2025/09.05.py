"""
Desafio: Distribuição de moedas
Crie um programa que simule a troca de um valor em reais para moedas. O programa deve:

Perguntar ao usuário um valor inteiro em reais (ex: 87).

Informar quantas moedas de R$1, R$0,50, R$0,25, R$0,10, R$0,05 e R$0,01 são necessárias para formar esse valor, usando o menor número possível de moedas.

Observação:
Para facilitar, considere que o usuário vai digitar o valor em centavos (ex: R$ 87,36 será digitado como 8736 centavos).

Use divisão inteira e resto para calcular a quantidade de cada moeda.
"""
v = float(input("Insira um valor: "))
m1 = v // 1
r = v % 1
m050 = r // 0.5
r = r % 0.5
m025 = r // 0.25
r = r % 0.25
m010 = r // 0.10
r = r % 0.10
m005 = r // 0.05
r = r % 0.05
m001 = r
print(f"Serão {m1} moedas de R$1")
print(f"Serão {m050} moedas de R$0,50")
print(f"Serão {m025} moedas de R$0,25")
print(f"Serão {m010} moedas de R$0,10")
print(f"Serão {m005} moedas de R$0,05 e")
print(f"Serão {m001} moedas de R$0,01.")