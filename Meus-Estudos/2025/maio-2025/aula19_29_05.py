#tuplas ()
#listas []
#dicionários {}
"""
dados1 = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
"""
filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}.')
