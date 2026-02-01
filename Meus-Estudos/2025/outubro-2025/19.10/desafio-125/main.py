"""
Faça uma classe Carro com atributos marca,
modelo e velocidade. Crie métodos acelerar
(que aumenta a velocidade) e frear
(que diminui a velocidade).
"""
from classes import Carro

c1 = Carro('Nissan', 'Sedan', '')
print('Carro:', c1.marca, c1.modelo)
c1.acelerar()
c1.frear()
