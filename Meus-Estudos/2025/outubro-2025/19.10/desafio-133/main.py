"""
Faça uma classe Pessoa com atributos nome e altura,
e um método mostrar_informacoes().
"""
from classes import Pessoa

p1 = Pessoa('Fin', 1.89)
p1.mostrar_informacoes()
p1.nome = 'Kyle'
p1.altura = 1.68
print()
p1.mostrar_informacoes()