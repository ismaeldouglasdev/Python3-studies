"""Exercício: Palíndromo com Números (exercicio do perplexity)
Descrição:
Escreva um programa que verifique se uma sequência de números
(como uma string) é um palíndromo. O programa deve ignorar espaços
e considerar apenas os dígitos.
Requisitos:
O programa deve solicitar ao usuário que
insira uma sequência de números.
O programa deve normalizar a
entrada, removendo espaços.
O programa deve verificar se
a sequência é um palíndromo.
O programa deve exibir uma mensagem
informando se a sequência é ou não um palíndromo."""
n = input('Insira os numeros: ')
n_norm = ""
for char in n:
    if char.isalnum():
        n_norm += char.lower()
if n_norm == n_norm[::-1]:
    print('Essa é uma sequência palíndromo!')
else:
    print('Essa sequência não é um palíndromo.')