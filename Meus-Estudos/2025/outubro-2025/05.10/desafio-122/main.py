"""
Desafio 122 — Programação Orientada a Objetos em Python:
Classes, Métodos e Encapsulamento

Objetivo:
Praticar a criação de classes, atributos privados,
métodos getters/setters e outros métodos básicos
com encapsulamento.

Requisitos:
1. Criar uma classe Pessoa com atributos privados:
   - nome
   - idade
   - peso

2. Implementar:
   - Construtor para inicializar os atributos
   - Métodos getters e setters para acessar e modificar
   os atributos de forma controlada
   - Método falar() que exiba uma frase simples
    com o nome da pessoa
   - Método envelhecer() que aumenta a idade em 1 ano
   - Método engordar(peso) que aumenta o peso da pessoa
   - Método emagrecer(peso) que diminui o peso da pessoa

3. Criar pelo menos 2 objetos da classe Pessoa
com valores iniciais diferentes.

4. Simular interações no script:
   - Fazer as pessoas falarem
   - Envelhecer, engordar e emagrecer
   - Exibir os valores atualizados dos atributos

Este desafio ajudará a entender os conceitos
básicos de encapsulamento e manipulação de
atributos em classes Python.
"""
from Pessoa import Pessoa

p1 = Pessoa('Narciso', 19, 90)
p2 = Pessoa('Zucker', 23, 70)

