class Pessoa:
    # Chamada de Super-classe.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):
    # Chamada de Sub-classe (Classes filhas)
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa):
    # Chamada de Sub-classe
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')
