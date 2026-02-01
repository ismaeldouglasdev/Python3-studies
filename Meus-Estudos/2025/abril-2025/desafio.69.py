"""
crie um programa que leia a idade e o sexo
de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer
ou não continuar. no final mostre:

a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.
"""
a = 0
b = 0
c = 0
sexo = ''
q = ''
print('-='*10)
print('Cadastro do governo')
print('-='*10)
while True:
    while True:
        print('CADASTRE UMA PESSOA')
        print('-='*10)
        idade = input('\nQual a idade? ')
        try:
            idade = int(idade)
            if idade > 18:
                a += 1
            break
        except ValueError:
            print('--' * 10)
            print('Digite um número válido!')
    while True:
        sexo = input('\nQual o sexo (m/f)? ')
        if sexo == 'm':
            b += 1
        if sexo == 'f' and idade < 20:
            c += 1
        print('--'*10)
        if sexo != 'm' and sexo != 'f':
            print('Digite uma resposta válida!')
        if sexo == 'm' or sexo == 'f':
            break
    while True:
        q = input('\nQuer continuar? (s/n): ')
        print('--'*10)
        if q != 'n' and q != 's':
            print('Digite uma respota válida!')
        if q == 's' or q == 'n':
            break
        q = ''
    if q == 'n':
        break
print('-='*10)
print('FIM DO PROGRAMA')
print('-='*10)
if a > 1:
    print(f'\n{a} pessoas tem mais de 18 anos;')
    print(f'foram cadastrados {b} homens.')
    print(f'e {c} mulheres têm menos de 20 anos.')
elif a <= 1 and idade < 18:
    a = 'nenhuma'
    print(f'\n{a} pessoa tem mais de 18 anos;')
    print(f'foram cadastrados {b} homens.')
    print(f'e {c} mulher tem menos de 20 anos.')
elif a <= 1 and idade > 18 and sexo != 'm':
    print(f'\n{a} pessoa tem mais de 18 anos;')
    print(f'foram cadastrados {b} homens.')
    print(f'e {c} mulher tem menos de 20 anos.')
elif a <= 1 and idade > 18 and sexo == 'm':
    c = 'nenhuma'
    print(f'\n{a} pessoa tem mais de 18 anos;')
    print(f'foi cadastrado apenas {b} homem')
    print(f'e {c} mulher tem menos de 20 anos.')

