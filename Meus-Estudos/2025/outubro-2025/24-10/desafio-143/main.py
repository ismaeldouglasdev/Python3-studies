"""
Leitura e escrita de arquivos:
Abra um arquivo de texto, conte a
quantidade de linhas e salve essa
informação em outro arquivo.
Dica: Use função open() com modos de
leitura e escrita.
"""
import os

arq = os.open("arq.txt", os.O_RDONLY)

linhas = 0
buffer_size = 1024

while True:
    # Leia um bloco de bytes
    bytes_lidos = os.read(arq, buffer_size)
    if not bytes_lidos:
        break # fim do arquivo

    # conte as quebras de linha nesse bloco
    linhas += bytes_lidos.count(b'\n')

os.close(arq)
print(f'Total de linhas: {linhas}')
