class Pessoa:
    def __init__(self, nome, idade, peso, falar=False):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__falar = falar

    @property
    def nome(self):
        return f'Nome: {self.__nome}.'

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.replace('', '')

    @property
    def idade(self):
        return f'A idade de {self.__nome} é {self.__idade}.'

    @idade.setter
    def idade(self, idade):
        try:
            if idade >= 0:
                self.__idade = idade
            else:
                print('\033[31mIdade Inválida\33[0m')
        except (TypeError, ValueError):
            print('\33[31mIdade Inválida\33[0m')

    @property
    def peso(self):
        return f'O peso de {self.__nome} é {self.__peso}.'

    @peso.setter
    def peso(self, peso):
        try:
            if peso >= 0:
                self.__peso = peso
            else:
                print('\033[31mPeso Inválido\33[0m')
        except (TypeError, ValueError):
            print('\33[31mPeso Inválido\33[0m')

    def falar(self, assunto):
        if self.__falar:
            print(f'{self.__nome} já está falando sobre {assunto}.')
        self.__falar = True
        print(f'{self.__nome} está falando sobre {assunto}.')

    def parar_falar(self):
        if self.__falar:
            self.__falar = False
            return print(f'{self.__nome} parou de falar.')
        print(f'{self.__nome} não está falando.')

    def envelhecer(self):
        self.__idade += 1
        print(f'A idade de {self.__nome} agora é {self.__idade}.')

    def engordar(self, peso):
        self.__peso += peso
        print(f'O peso de {self.__nome} agora é {self.__peso}')

    def emagrecer(self, peso):
        self.__peso -= peso
        print(f'O peso de {self.__nome} agora é {self.__peso}')
