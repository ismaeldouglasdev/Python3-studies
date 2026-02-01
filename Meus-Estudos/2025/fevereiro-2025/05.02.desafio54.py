"""
aula 13: laços de repetição: desafio 54
"""
"""
crie um programa que leia o ano
de nascimento de sete pessoas.
no final, mostre quantas pessoas
ainda não atingiram a maioridade
e quantas já são maiores.
"""
p1 = 0
p2 = 0
for i in range(1, 8):
    p = int(input('Insira ano de nascimento: '))
    if 2025 - p < 21:
        p = 1
        p1 += p
    else:
        p = 1
        p2 += p
print("""\n{} pessoas ainda
não atingiram a maioridade e 
{} já atingiram a maioridade.""".format(p1, p2))

