"""
Contar arquivos por formato:
Conte quantos arquivos .jpg existem
em um diretório e imprima o total.
Dica: Use laço e os.path.splitext().
"""
import os

folder = r"C:\Users\ismae\Downloads\Imagens"
archives = os.listdir(folder)
c = 0
d = 0

for archive in archives:
    root, ext = os.path.splitext(archive)
    if ext == ".png":
        c += 1
    if ext == ".jpg":
        d += 1
print(f'O total de arquivos .jpg é {d}')
print(f'O total de arquivos .png é {c}')
print(f'O total de arquivos de imagens detectados foi {d + c}')

