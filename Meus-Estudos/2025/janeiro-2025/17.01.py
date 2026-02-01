nome = str(input('Qual é seu nome? '))
if nome == 'Ismael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Julia':
    print('Belo nome feminino!')
else:
    print('Seu nome é comum.')
print('Tenha um bom dia, {}!'.format(nome))
