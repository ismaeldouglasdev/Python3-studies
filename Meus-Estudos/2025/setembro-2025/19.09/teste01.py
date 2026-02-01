import io
import sys

# Salvar a saída padrão atual (a tela)
old_stdout = sys.stdout

# Criar uma "caixa" para capturar texto (uma espécie de arquivo em memória)
mystdout = io.StringIO()

# Redirecionar a saída padrão para nossa caixa/memória
sys.stdout = mystdout

# Executar o help, que normalmente imprime na tela, mas agora vai para mystdout
help(len)  # exemplo: ajuda da classe string

# Restaurar a saída padrão para a tela
sys.stdout = old_stdout

# Pegar o conteúdo capturado como string
help_text = mystdout.getvalue()

# Mostrar o texto capturado
print(help_text)
