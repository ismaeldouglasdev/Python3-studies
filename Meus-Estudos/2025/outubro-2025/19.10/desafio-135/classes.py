class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = dict()
        self.historico_consultas['Data:'] = []
        self.historico_consultas['Numero:'] = []
        self.historico_consultas['Nome:'] = []

    def adicionar_consulta(self):
        q = input('Insira a data da consulta: ')
        self.historico_consultas['Data:'].append(q)
        n = input('Insira o N° da consulta: ')
        self.historico_consultas['Numero:'].append(n)
        x = input('Digite o nome: ')
        self.historico_consultas['Nome:'].append(x)

    def listar_consultas(self):
        for a in self.historico_consultas.keys():
            print(f'\033[33m{str(a):^15}\033[0m', end='')
        print()
        n = len(next(iter(self.historico_consultas.values())))
        for i in range(n):
            for b in self.historico_consultas.values():
                print(f'\033[35m{b[i]:^15}\033[0m', end='')
            print()
