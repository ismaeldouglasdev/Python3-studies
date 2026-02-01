"""
Associação: Crie duas classes, Pessoa e Carro.
Faça com que Pessoa possa possuir um ou mais objetos Carro,
mas sem que Pessoa seja responsável por criar os carros.
Demonstre que os carros podem existir independentemente.
"""
from classes import Pessoa, Carro

p1 = Pessoa('Julia', 25)
p1.possuir_carro('Toyota', 'Azul')
print(p1.nome, 'possui:', p1.mostrar_carros())

c1 = Carro('Ferrari', 'Vermelha')
print(c1.carro_independente())
