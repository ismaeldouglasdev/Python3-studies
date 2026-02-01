"""
Faça uma classe ContaBancária com
atributos numero, titular e saldo.
Implemente métodos depositar e sacar.
"""
from classes import ContaBancaria

c = ContaBancaria(120007, 'Julia', 0)
c.depositar()
c.sacar()
c.depositar()
c.sacar()
c.depositar()
c.sacar()
