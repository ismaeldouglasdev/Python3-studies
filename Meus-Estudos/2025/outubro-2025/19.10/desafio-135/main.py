"""
Faça uma classe Paciente com atributos nome,
idade, historico_consultas (lista). Métodos
para adicionar e listar consultas.
"""
from classes import Paciente

p1 = Paciente('Andro', 29)
while True:
    p1.adicionar_consulta()
    q1 = input('Quer ver a lista?')
    if q1.lower() in ['s', 'sim']:
        p1.listar_consultas()
    q = input('Quer continuar?')
    if q.lower() in ['n', 'nao', 'não']:
        break
