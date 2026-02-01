"""
Crie uma classe Circulo com atributo raio,
método area e circunferencia.
"""
from classes import Circulo

c1 = Circulo(4)
c1.raio = 2
print(c1.raio)
print(c1.area())
print(c1.circunferencia())
print()
c1.raio = 8
print(c1.raio)
print(c1.area())
print(c1.circunferencia())
