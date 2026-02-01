class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def valor_em_estoque(self):
        vl = self.preco * self.quantidade_em_estoque
        print(f'O valor total em estoque de {self.nome} é R${vl}')
