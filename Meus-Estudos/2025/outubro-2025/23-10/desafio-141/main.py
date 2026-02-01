"""
Mover arquivos por extensão:
Mova todos os arquivos
.txt de uma pasta para outra pasta
chamada Textos.
Dica: Use os.listdir(), shutil.move()
e crie a pasta destino se necessário.
"""
import os
import shutil

pasta_o = r"C:\Users/ismae/Desktop/code study/MeusProjetos/Python-3-studies/Meus-Estudos/outubro-2025/23-10/pasta-o"
pasta_d = r"C:/Users/ismae/Desktop/code study/MeusProjetos/Python-3-studies/Meus-Estudos/outubro-2025/23-10/pasta-d"

# Criar a pasta destino se não existir
os.makedirs(pasta_d, exist_ok=True)

# Lista todos os itens da pasta de origem
itens = os.listdir(pasta_o)

for item in itens:
    caminho_item = os.path.join(pasta_o, item)
    # Verifica se é arquivo e sua extensão é .txt
    if os.path.isfile(caminho_item) and item.lower().endswith(".txt"):
        caminho_destino = os.path.join(pasta_d, item)
        shutil.move(caminho_item, caminho_destino)
        print(f'Movido: {item}')
