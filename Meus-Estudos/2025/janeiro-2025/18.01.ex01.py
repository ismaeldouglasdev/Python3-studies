"""
(desafio 43)
Desenvolva uma lógica que leia o peso
e a altura de uma pessoa, e calcule seu
IMC e mostre seu status, de acordo com a tabela
abaixo:

- Abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
"""
print('Bem-vindo(a) à calculadora de IMC (índice de massa corporal)')
peso = float(input('Qual é o seu peso? '))
altura = float(input('E qual é a sua altura? '))
imc = peso/altura ** 2
print('Seu IMC é {:.1f}!'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso :(')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal :)')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')


