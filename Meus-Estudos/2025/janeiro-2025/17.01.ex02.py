""""
Escreva um programa que leia um número
inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal """
n = int(input('Escreva um número: '))
print('''Agora escolha a base de conversão:
          digite [1] para binário
          digite [2] para octal
          digite [3] para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')



