n = input('Qual seu nome? ')
cores = {'limpa':'\033[m',
         'azul':'\033[34m \033[m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'}
print('Olá prazer em te conhecer {}{}{}\033[m'.format(cores['pretoebranco'],n,cores['pretoebranco']))