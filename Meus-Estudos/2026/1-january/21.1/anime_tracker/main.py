"""
Docstring for 2026.1-january.21.1.main

Desafio: Organizador de Anime Tracker
Crie um script que gerencie sua lista de anime. Salve em anime_tracker.py:

Funcionalidades obrigatórias:
Adicionar anime interativamente (input())
Mostrar estatísticas: total por status
Salvar/carregar em JSON (json module)
"""
import logica


print("Anime Tracker")
while True:
    animes = logica.carregar_animes()
    q = input( "Opções:\n" 
    "[0] Salvar lista. \n"
    "[1] Listar rank de animes.\n"
    "[2] Adicionar um novo anime.\n"
    "[3] Excluir um anime do ranking.\n"
    "[4] Adicionar um anime dropado.\n" 
    "[5] Adicionar um anime pra assistir depois.\n"
    "[6] Mostrar Estatísticas.\n" \
    "[X] Sair.\n"
    "O que deseja fazer? \n")
    if q == '0':
        logica.salvar_lista(animes)
    if q == '1':
        logica.mostrar_estatisticas(),
        logica.listar_animes()
    if q == '2':
        logica.adicionar_anime()
    if q == '3':
        logica.excluir_anime()
    if q == '4':
        logica.add_dropado()
    if q == '5':
        logica.add_assistir_dps()
    if q == '6':
        logica.mostrar_estatisticas()
    if q.lower() == 'x':
        print('-'*50)
        print('Obrigado! ^^')
        print('-'*50)
        break