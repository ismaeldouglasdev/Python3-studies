# Para salvar o dicionário em arquivo JSON
def salvar_dicionario(nome_arquivo, pessoas):
    from json import dump
    with open(nome_arquivo, 'w') as arquivo:
        dump(pessoas, arquivo)


def carregar_dicionario(nome_arquivo):
    from json import load
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return load(arquivo)
    except FileNotFoundError:
        return {}


def add_pessoas(pessoas, a, b):
    pessoas[a] = int(b)


def mostrar_pessoas(pessoas):
    print(f'-'*40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print(f'-'*40)
    for a, b in pessoas.items():
        print(f'{a:<20}{b:>10} anos')
    print(f'-'*40)


def menu_principal():
    nome_arquivo = 'dados.json'
    pessoas = carregar_dicionario(nome_arquivo)
    while True:
        print('-'*40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-'*40)
        print('\033[33m1 -\033[0m \033[34mVer pessoas cadastradas\033[0m')
        print('\033[33m2 -\033[0m \033[34mCadastrar nova pessoa\033[0m')
        print('\033[33m3 -\033[0m \033[34mSair do sistema\033[0m')
        print('-'*40)
        try:
            x = int(input('\033[33mSua Opção: \033[0m'))
            if x == 1:
                mostrar_pessoas(pessoas)
            elif x == 2:
                while True:
                    a = input('Nome: ')
                    if a.isnumeric():
                        print('\033[31mPor favor, digite um valor válido.\033[0m')
                    else:
                        break
                while True:
                    try:
                        b = int(input('idade: '))
                        break
                    except ValueError:
                        print('\033[31mPor favor, digite um valor válido.\033[0m')
                add_pessoas(pessoas, a, b)
                salvar_dicionario('dados.json', pessoas)
                print(f'\033[32mNovo registro de {a} adicionado.\033[0m')
            elif x == 3:
                print(f'-' * 40)
                print(f'{"Saindo do sistema... Até logo!":^40}')
                print(f'-' * 40)
                break
            else:
                print('\033[31mOpção inválida, tente novamente.\033[0m')
        except ValueError:
            print('\033[31mPor favor, digite um número válido.\033[0m')

