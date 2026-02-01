"""
aula 13: laços de repetição: desafio 47
"""
"""
crie um programa que mostre na tela todos 
os números pares que estão no intervalo
entre 1 e 50.
"""
print('Aqui estão, todos os números pares entre 1 e 50:')
for c in range(1,51,):
    if c % 2 == 0:
        print(c)
