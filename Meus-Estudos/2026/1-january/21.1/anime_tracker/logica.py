import json
ranking = "ranking_animes.json"


def carregar_animes():
    #Carrega lista do JSON.
    try:
        with open(ranking, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if data else [] # retorna [] se vazio
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # retorna lista vazia se arquivo não existe


def salvar_lista(animes):
    #Salva lista no JSON.
    with open(ranking, "w", encoding="utf-8") as f:
        json.dump(animes, f, indent=2, ensure_ascii=False)


def listar_animes():
    #Lista todos os animes (opção 1).
    animes = carregar_animes()

    if not animes:
        print("📭 Nenhum anime cadastrado ainda!")
        print("="*80)
        return
    
    animes = ordenar_animes(animes)

    status_títulos = {
        "planejado": "⏳ PLANEJADOS",
        "assistindo": "📺 ASSISTINDO",
        "completo": "✅ COMPLETOS",
        "dropado": "💔 DROPADOS"
    }

    print(f"{'#':>3} | {'NOME':<42} | {'NOTA':>5} | {'STATUS':<10}")
    print("="*80)

    status_atual = None

    for i, anime in enumerate(animes, 1):
        if anime["status"] != status_atual:
            print(f"\n{status_títulos.get(anime['status'], anime['status'].upper()):^80}")
            print('-'*80)
            status_atual = anime["status"]

        nome_cortado = (anime["nome"][:38] + "...") if len(anime["nome"]) > 40 else anime["nome"]

        print(f'{i:>2}. {nome_cortado:<40} | Nota: {anime["nota"]:^5} | Status: {anime["status"]:<10}')

    

def adicionar_anime():
    #adiciona novo anime via input() interativo.
    print('='*100)
    nome = input('Nome do anime: ')
    nota = float(input('Nota: '))
    status = input('Status (assistindo/completo/planejado): ')

    animes = carregar_animes()
    animes.append({"nome": nome, "nota": nota, "status": status})
    animes = ordenar_animes(animes)
    salvar_lista(animes)
    print(f'{nome} adicionado!')
    print('='*100)



def excluir_anime():
    #exclui anime por indice (opção 3).
    animes = carregar_animes()
    listar_animes(animes)
    idx = int(input("indice para excluir: ")) - 1
    if 0 <= idx < len(animes):
        removido = animes.pop(idx)
        animes = ordenar_animes(animes)
        salvar_lista(animes)
        print(f'{removido["nome"]} excluído!')
        print('='*100)

    else:
        print('Índice invalido.')
        print('='*100)


def add_dropado():
    #adiciona com status 'dropado' (opção 4, extensão).
    print('='*100)
    nome = input('Nome do anime dropado: ')
    animes = carregar_animes()
    animes.append({"nome": nome, "nota":"--", "status": "dropado"})
    animes = ordenar_animes(animes)
    salvar_lista(animes)
    print(f'{nome} marcado como dropado.')
    print('='*100)

def add_assistir_dps():
    #adiciona como 'planejado' (opção 5).
    print('='*100)
    nome = input('Nome do anime para assistir depois: ')
    animes = carregar_animes()
    animes.append({"nome": nome, "nota":"--", "status": "planejado"})
    salvar_lista(animes)
    print(f'{nome} adicionado aos planejados!')
    print('='*100)


def mostrar_estatisticas():
    #total por status (opção 6)
    animes = carregar_animes()
    stats = {"assistindo": 0, "completo": 0, "planejado": 0, "dropado": 0}
    for anime in animes:
        stats[anime["status"]] += 1
    print('='*100)
    print("Estatísticas:")
    for status, count in stats.items():
        print(f'- {status}: {count}')
    print('='*100)


def ordenar_animes(animes):
    #Ordena: 1° por status (planejado->assistindo->completo->dropado), 2° por nota DESC.

    # Ordem prioritária dos status (0=maior prioridade)
    ordem_status = {
        "planejado": 1,
        "assistindo": 3,
        "completo": 0,
        "dropado": 2
    }

    def chave_ordenacao(anime):
        return (ordem_status.get(anime["status"], 99), - float(anime["nota"]))

    return sorted(animes, key=chave_ordenacao)
    
