class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carros = []

    def possuir_carro(self, marca, cor):
        self.carros.append(Carro(marca, cor))

    def mostrar_carros(self):
        for carros in self.carros:
            return f'{carros.marca} {carros.cor}'


class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def carro_independente(self):
        return f'O carro {self.marca} de cor {self.cor} é independente da Classe Pessoa'
