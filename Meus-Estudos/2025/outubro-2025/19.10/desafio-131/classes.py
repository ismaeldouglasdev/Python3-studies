class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def area(self):
        area = self.tamanho_lado * self.tamanho_lado
        print(f'A area é {area}m²')
