class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return f'O raio do círculo é {self._raio}m'

    @raio.setter
    def raio(self, valor):
        self._raio = valor

    def area(self):
        area = 3.1415 * (self._raio * self._raio)
        return f'A área desse círculo é {area:.2f}m²'

    def circunferencia(self):
        circunferencia = 2 * (3.1415 * self._raio)
        return f'A circunferência desse círculo é {circunferencia:.2f}m'
