import io
import sys
from colorama import init, Fore, Back

init(autoreset=True)

# Captura saída do help numa string
old_stdout = sys.stdout
sys.stdout = mystdout = io.StringIO()

help(str)

sys.stdout = old_stdout

help_text = mystdout.getvalue()

# Imprime o texto do help em uma cor
print(Back.WHITE + help_text)
