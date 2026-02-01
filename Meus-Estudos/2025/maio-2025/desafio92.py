"""
Crie um programa que leia nome,
ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai
se aposentar (considerando que demora 35 anos
de contribuição para se aposentar).
"""
pessoas = dict()
pessoas['nome'] = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
idade = 2025 - ano
pessoas['idade'] = idade
pessoas['ctps'] = ctps = input('Carteira de trabalho[0 caso não tenha]: ')
if ctps != 0:
    pessoas['contratação'] = ac = int(input('Ano de contratação: '))
    pessoas['salário'] = input('Salário: R$ ')
    ano_ap_p = 2025 - ac
    aposentadoria = 35 - ano_ap_p
    print(f"""Olá {pessoas["nome"]}!
Você tem {pessoas["idade"]} anos,
Sua carteira de trabalho é {pessoas["ctps"]},
e você vai se aposentar daqui a {aposentadoria} anos.""")
else:
    print(f'Olá {pessoas["nome"]}!'
          f'Você tem {pessoas["idade"]} anos.'
          f'e você não tem carteira de trabalho.')



