"""
Crie uma classe Livro com atributos titulo,
autor e numero_pags. Adicione métodos emprestar e
devolver com um atributo de controle de disponibilidade.
"""
from classes import Livro

a = Livro('Alice no país das maravilhas', 'Frank Rose', 23)
a.emprestar()
a.emprestar()
a.devolver()
a.devolver()
