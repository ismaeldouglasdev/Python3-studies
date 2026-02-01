class Pessoa:
    def __init__(self, nome, idade, altura, peso, falar=False, comer=False, dormir=False):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.falar = falar
        self.comer = comer
        self.dormir = dormir

    def imprimir(self):
        return print(f'{self.nome} tem {self.idade} anos, '
                     f'{self.altura:.2f} de altura e {self.peso} kg de peso.')

    def falando(self, assunto):
        if self.falar:
            return print(f'{self.nome} já está falando.')
        if self.comer:
            return print(f'{self.nome} não pode falar enquanto come.')
        if self.dormir:
            return print(f'{self.nome} não pode falar enquanto dorme.')
        self.falar = True
        return print(f'{self.nome} começou a falar sobre {assunto}')

    def comendo(self):
        if self.comer:
            return print(f'{self.nome} já está comendo.')
        if self.falar:
            return print(f'{self.nome} não pode comer enquanto fala.')
        if self.dormir:
            return print(f'{self.nome} não pode comer enquanto dorme.')
        self.comer = True
        return print(f'{self.nome} começou a comer.')

    def parar_comer(self):
        if self.comer:
            self.comer = False
            return print(f'{self.nome} parou de comer.')
        return print(f'{self.nome} não está comendo.')

    def parar_falar(self):
        if self.falar:
            self.falar = False
            return print(f'{self.nome} parou de falar.')
        return print(f'{self.nome} não está falando.')

    def dormindo(self):
        if self.dormir:
            return print(f'{self.nome} já está dormindo.')
        if self.falar:
            return print(f'{self.nome} não pode dormir enquanto fala.')
        if self.comer:
            return print(f'{self.nome} não pode dormir enquanto come.')
        self.dormir = True
        return print(f'{self.nome} começou a dormir.')

    def parar_dormir(self):
        if self.dormir:
            self.dormir = False
            return print(f'{self.nome} acordou.')
        return print(f'{self.nome} não está dormindo.')

    def imc(self):
        return print(f'O IMC de {self.nome} é {self.peso/self.altura**2:.2f}')
