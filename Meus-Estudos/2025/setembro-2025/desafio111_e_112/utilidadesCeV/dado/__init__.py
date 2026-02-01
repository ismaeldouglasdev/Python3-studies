def leia_dinheiro():
    while True:
        x = input('Digite o preço: R$ ')
        try:
            y = float(x.replace(',', '.'))
            return y
        except ValueError:
            print(f'\033[31mERRO: "{x}" é um preço inválido!\033[0m')
