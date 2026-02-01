class Livro:
    def __init__(self, titulo, autor, numero_pags):
        self.titulo = titulo
        self.autor = autor
        self.numero_pags = numero_pags
        self.disponibilidade = True

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            return print('O livro foi emprestado!')
        print('O livro já foi emprestado, não está disponível.')

    def devolver(self):
        if self.disponibilidade:
            return print('O livro já foi devolvido, e está disponível.')
        print('O livro foi devolvido!')
        self.disponibilidade = True
