class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calc_area(self):
        self.largura = int(input('Insira a largura (m): '))
        self.altura = int(input('Insira a altura (m): '))
        area = self.largura * self.altura
        print(f'A area é de {area} metros.')

    def calc_perimetro(self):
        self.largura = int(input('Insira a largura (m): '))
        self.altura = int(input('Insira a altura (m): '))
        perimetro = 2 * (self.largura + self.altura)
        print(f'O perimetro é de {perimetro} metros.')