f = input('Digite uma frase: ')
palavras = f.split()
cont = {}
for palavra in palavras:
    if palavra in cont:
        cont[palavra] += 1
    else:
        cont[palavra] = 1
print(cont)