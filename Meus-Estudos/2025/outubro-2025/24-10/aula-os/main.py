import os

# absoluto = (r"C:\Users\ismae\Desktop\code study\MeusProjetos\Python-3-studies\Meus-Estudos\outubro-2025\24-10\aula-os"
#            r"\main.py")
# relativo = r"Meus-Estudos/outubro-2025/24-10/aula-os/main.py"

"""DATA_DIR = "data"
print(os.path.abspath(DATA_DIR))

caminho = os.path.join(os.path.abspath(DATA_DIR), "data.txt")
print(caminho)

print(os.listdir(r"C:/Users\ismae\Desktop/
code study\MeusProjetos\Python-3-studies\
Meus-Estudos\setembro-2025"))

modulos_python = []
for nome in os.listdir(r"C:/Users\ismae\Desktop/
code study\MeusProjetos\Python-3-studies\Meus-Estudos
\setembro-2025"):
    if nome.endswith(".py"):
        modulos_python.append(nome)
print(modulos_python)

print(os.path.join(
    os.path.abspath('.'), 'data', 'data.txt'))"""

OUTPUT_DIR = "saídas"
nomearquivo = "mensagem.txt"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(os.path.join(OUTPUT_DIR, nomearquivo), 'w') as arq:
    arq.write("Teste-999999")
