class Pessoa:
    def __init__(self, nome, altura):
        self._nome = nome
        self._altura = altura

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def mostrar_informacoes(self):
        return print(f'Nome: {self._nome}, Altura: {self._altura}')

