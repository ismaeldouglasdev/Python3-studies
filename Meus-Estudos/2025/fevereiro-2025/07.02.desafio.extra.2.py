"""
Desafio:
Crie um programa que receba
como entrada o primeiro termo (a₁)
e a razão (r) de uma Progressão Geométrica (PG).
O programa deve calcular e exibir os n primeiros
termos da PG usando a estrutura while.
O valor de n (o número de termos a serem exibidos)
também deve ser fornecido pelo usuário.
Dicas:
Lembre-se que, em uma PG, cada termo é
obtido multiplicando o termo anterior pela razão.
Na PA, somávamos a razão; na PG, multiplicamos.
A fórmula geral para o termo n
de uma PG é: aₙ = a₁ * r^(n-1) ,
onde a₁ é o primeiro termo e r é a razão.
No entanto, você pode construir a PG de
forma iterativa (sem usar a fórmula diretamente)
para praticar o uso do while.
Certifique-se de incluir uma mensagem
final indicando o fim da progressão.
"""
print('Gerador de PG')
print('-=-' * 10)
a1 = int(input('insira o primeiro termo: '))
r = int(input('Insira a razão: '))
n = int(input('Insira a quantidade de termos: '))
t = a1
c = 1
while c <= n:
    print('{} -> '.format(t), end='')
    t *= r
    c += 1
print('FIM!')