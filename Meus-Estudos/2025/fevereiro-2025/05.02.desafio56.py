"""
aula 13: laços de repetição: desafio 56
"""
"""
desenvolva um programa que leia
o nome, idade e sexo de 4 pessoas.
no final do programa, mostre:

- a média de idade do grupo;
- qual é o nome do homem mais velho.
- quantas mulheres têm menos de 20 anos.
"""
si = 0
iv = 0
hv = ''
m = 0
for c in range(1,5):
    n = input('Qual o nome? ')
    i = int(input('Qual a idade? '))
    s = input('Qual é o sexo? ').lower()
    if i > iv and s == 'masculino':
        iv = i
        hv = n
    if i < 20 and s == 'feminino':
        i = 1
        m += i
    si += i
im = si/4
print("""A idade média do grupo é {},
o homem mais velho chamado {} tem {} anos.
{} mulheres têm menos de 20 anos.""".format(im,hv,iv, m))

