class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        a = int(input('Quanto deseja depositar? '))
        self.saldo += a
        print(f'Saldo atual: {self.saldo}')

    def sacar(self):
        a = int(input('Quanto deseja sacar? '))
        self.saldo -= a
        print(f'Saldo atual: {self.saldo}')
