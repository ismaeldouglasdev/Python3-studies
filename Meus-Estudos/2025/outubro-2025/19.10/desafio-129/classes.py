class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.media = None

    def inserir_nota(self):
        q = ''
        while q.lower() not in ['n', 'não', 'nao']:
            entrada = input('\033[35mInsira uma nota: \033[0m')
            entrada = entrada.replace(',', '.')
            try:
                ef = float(entrada)
                ef2 = str(ef).replace('.', ',')
                self.notas.append(ef2)
                q = input('\033[33mQuer continuar? \033[0m')
            except ValueError:
                print('\033[31mValor inválido! tente novamente.\033[0m')

    def calc_media(self):
        c = 0
        for notas in self.notas:
            notas = notas.replace(',', '.')
            notasf = float(notas)
            c += notasf
        self.media = c/len(self.notas)
        print(f'\033[34mA media é {self.media:.2f}\033[0m')

    def situacao(self):
        if self.media >= 7:
            return print(f'\033[32mA média de {self.nome} é {self.media:.2f} '
                         f'portanto sua situação é APROVADO(A)!\033[0m')
        print(f'\033[31mA média de {self.nome} é {self.media:.2f} e '
              f'por isso sua situação é REPROVADO(A)!\033[0m')
