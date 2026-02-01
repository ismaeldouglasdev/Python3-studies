class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = 'A velocidade aumentou!'
        print(self.velocidade)

    def frear(self):
        self.velocidade = 'A velocidade diminuiu!'
        print(self.velocidade)