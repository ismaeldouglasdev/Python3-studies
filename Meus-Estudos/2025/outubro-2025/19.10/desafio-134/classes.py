class Funcionario:
    def __init__(self, nome, salario, cargos):
        self.nome = nome
        self.salario = salario
        self.cargos = cargos

    def aumentar_salario(self):
        q = int(input('Deseja aumentar em quanto o salário? '))
        self.salario += q
        return print(f'O salário de {self.nome} agora é {self.salario}')