"""
Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e impares
em ordem crescente.
"""
# inputando e iterando os valores:
valores = [[], []]
for i in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

# ordenando os valores.
valores[0].sort()
valores[1].sort()

# imprimindo as listas de forma ordenada e formatada.
print(f'Números pares: {valores[0]}')
print(f'Números ímpares: {valores[1]}')
