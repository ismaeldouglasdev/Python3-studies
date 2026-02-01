from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""


c1 = Cliente('Ana', 34)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 20)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()