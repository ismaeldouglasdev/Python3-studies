"""
Desafio 116: Feito
Criar uma classe Pessoa simples:
Implemente uma classe Pessoa que tenha os atributos
nome e idade, e um método que imprima uma mensagem
com nome e idade.
----------------------------
Desafio 117: Feito
Adicionar métodos de comportamento
Expanda a classe Pessoa para incluir métodos
falar(), comer() e dormir(), e mudem o
estado interno (por exemplo, indicador se está
comendo ou falando).
----------------------------
Desafio 118: Feito
Controlar estado interno com lógica
Modifique os métodos para não permitir que a pessoa
fale enquanto estiver comendo, e que não possa comer se já estiver comendo.
Implemente mensagens de aviso.
----------------------------
Desafio 119: Feito
Criar múltiplas instâncias independentes
Crie pelo menos duas instâncias da classe Pessoa
e demonstre que cada uma mantém seu próprio
estado independente (nome, o que está fazendo, etc).
----------------------------
Desafio 120: Feito
Implementar método especial init
Melhore a classe Pessoa para usar o método construtor
_init_ para inicializar atributos ao criar o objeto.
----------------------------
Desafio 121: Feito
Implementar atributos e métodos adicionais
Adicione atributos como altura e peso,
e métodos para calcular o IMC (índice de massa corporal).
"""
from pessoa import Pessoa

p1 = Pessoa('Ismael', 19, 1.80, 90)
p2 = Pessoa('Barbara', 19, 1.60, 50)
p1.imprimir()
p2.imprimir()
p1.imc()
p2.imc()
