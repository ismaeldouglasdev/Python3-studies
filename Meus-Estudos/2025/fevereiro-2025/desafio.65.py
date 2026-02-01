"""
O Desafio 65 do curso de Python pede para desenvolver um programa
que leia vários números inteiros pelo teclado.
O programa deve perguntar ao usuário se ele deseja continuar
a digitar números. No final, o programa deve mostrar:
A média entre todos os valores digitados
O maior valor digitado
O menor valor digitado
"""
r = ''
c = ma = n = me = t = 0
while r in 'Ss':
    n = int(input('Insira o número desejado: '))
    if c == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    c += 1
    t += n
    r = input('Deseja continuar adicionando números?(s/n): ')

print('Você digitou {} números, A média de todos os valores digitados é {}'.format(c, t/c))
print('O maior valor foi {} e o menor foi {}.'.format(ma, me))