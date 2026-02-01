"""
Crie um código em python que teste se o site
Pudim está acessível pelo computador usado.
"""
import requests

try:
    r = requests.get('https://www.pudim.com.br/', timeout=5)
    print(f'\033[32mO site do pudim foi acessado com sucesso! :)\033[m')
except Exception as erro:
    print(f'\033[31mO site do pudim não está disponível no momento! :/'
          f'\nErro: {erro}\033[m')
