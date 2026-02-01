class Triangulo:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def eh_valido(self):
        a, b, c = abs(self.a), abs(self.b), abs(self.c)
        if a < (b + c) and b < (a + c) and c < (a + b):
            print(f'O triangulo de lados {a}, {b} e {c} é valido')
            return True
        else:
            print(f'O triangulo de lados {a}, {b} e {c} é inválido.')
            return False

    def calc_area(self):
        if self.eh_valido:
            a, b, c = abs(self.a), abs(self.b), abs(self.c)
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            return f'A area é de {area:.2f}m'
        return 'Não é possivel calcular a área de um triangulo inválido.'
