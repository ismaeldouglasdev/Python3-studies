class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return f'A idade de {self.nome} é {self._idade}.'

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    def fazer_aniversario(self):
        self._idade += 1
        print(f'A idade de {self.nome} agora é {self._idade}.')

