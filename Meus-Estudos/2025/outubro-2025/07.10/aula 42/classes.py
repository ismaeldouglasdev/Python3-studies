class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for p in self.produtos:
            print(p.nome, p.valor)

    def soma_total(self):
        total = 0
        for p in self.produtos:
            total += p.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
