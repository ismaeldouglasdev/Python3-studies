"""
Adapte o código do desafio 107, criando
uma função adicional chamada moeda() que
consiga mostrar os valores como um valor
monetário formatado.
"""
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p))}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p))}')
