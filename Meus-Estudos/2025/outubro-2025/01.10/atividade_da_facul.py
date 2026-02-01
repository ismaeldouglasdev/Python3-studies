"""
Escreva um programa que leia um número inteiro N e gere uma
lista com N elementos aleatórios entre 10 e 50 (utilizando
a função randint mencionada
em um exercício anterior).
O programa deve exibir a lista gerada e também a mesma lista
com seus elementos ordenados em ordem crescente.

Além disso, há uma tarefa adicional que sugere corrigir a
solução para tratar o erro que ocorre quando o dado digitado
não for um número inteiro, usando o comando try-except para
lidar com exceções de conversão.

Como desafio, sugere-se também alterar o programa para que
a lista gerada não contenha valores duplicados, utilizando
os operadores in e not in para verificar e evitar duplicações.
"""
from random import randint
while True:
    try:
        n = int(input('Digite um número: '))
        lista_al = list()

        while len(lista_al) < n:
            numero_al = randint(10, 50)
            if numero_al not in lista_al:
                lista_al.append(numero_al)

        print(f'\33[32mlista gerada: {lista_al}\33[0m')
        lista_al.sort()
        print(f'\33[34mlista ordenada: {lista_al}\33[0m')
        break
    except ValueError:
        print('\33[31mErro! Digite um dado válido!\33[0m')
