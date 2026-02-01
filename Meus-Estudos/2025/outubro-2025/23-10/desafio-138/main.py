"""
Listar arquivos: Liste todos os arquivos
e pastas em um diretório especificado.
Dica: Use os.listdir() e os.path.isfile().
"""
import os

all_archives_ = "C:/Users/ismae/Desktop/code study/Arquivo/estudo de python/praticas de outubro"
all_folders_ = "C:/Users/ismae/Desktop/code study/Arquivo/estudo de python/"
arquivos = [f for f in os.listdir(all_archives_) if os.path.isfile(os.path.join(all_archives_, f))]
print('ARQUIVOS:')
for a in arquivos:
    print(f'\033[33m- Arquivo: {a}\033[0m')
pastas = [p for p in os.listdir(all_folders_) if os.path.isdir(os.path.join(all_folders_, p))]
print('\nPASTAS:')
for p in pastas:
    print(f'\033[32m- Pasta: {p}\033[0m')
