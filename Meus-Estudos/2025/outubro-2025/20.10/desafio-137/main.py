"""
Crie uma classe Triangulo com lados a, b, c.
Adicione método eh_valido() e calcular_area().
"""
from classes import Triangulo

t = Triangulo(3, 5, 3)
print(t.eh_valido())
f = t.calc_area()
print(f)
