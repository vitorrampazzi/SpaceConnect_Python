import csv
import time
from estruturas import ListaLigadaSatelites, FilaTelemetria, PilhaComandos
from algoritmos import quick_sort_satelites, busca_binaria


def carregar_dados_satelites(nome_arquivo):
    satelites = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as file:
            leitor_csv = csv.DictReader(file)
            for linha in leitor_csv:
                # Convertendo os IDs e altitudes para inteiros para facilitar ordenação depois
                linha['id'] = int(linha['id'])
                linha['altitude_km'] = int(linha['altitude_km'])
                satelites.append(linha)
        print(f"[SUCESSO] {len(satelites)} satélites carregados da base de dados.\n")
        return satelites
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{nome_arquivo}' não encontrado. Verifique o caminho.")
        return []
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema ao ler o arquivo: {e}")
        return []


if __name__ == "__main__":
    print("--- SISTEMA SPACECONNECT: RASTREAMENTO ORBITAL ---\n")

    dados_iniciais = carregar_dados_satelites('satelites_data.csv')

    catalogo_orbital = ListaLigadaSatelites()
    if dados_iniciais:
        for s in dados_iniciais:
            catalogo_orbital.adicionar(s)
        catalogo_orbital.exibir_todos()

    print("\n--- INICIANDO RECEPÇÃO DE TELEMETRIA (FILA) ---")
    fila_sinais = FilaTelemetria()

    pacote1 = {'id_satelite': 101, 'bateria': '98%', 'temperatura': '15C'}
    pacote2 = {'id_satelite': 105, 'bateria': '85%', 'temperatura': '18C'}
    pacote3 = {'id_satelite': 102, 'bateria': '100%', 'temperatura': '12C'}

    fila_sinais.enfileirar(pacote1)
    fila_sinais.enfileirar(pacote2)
    fila_sinais.enfileirar(pacote3)

    print(f"\nStatus: {fila_sinais.tamanho()} pacotes aguardando processamento na fila.\n")

    print("--- PROCESSANDO PACOTES ---")
    while not fila_sinais.esta_vazia():
        pacote_atual = fila_sinais.desenfileirar()
        print(
            f"[PROCESSANDO] Lendo dados do Satélite ID {pacote_atual['id_satelite']} | Bateria: {pacote_atual['bateria']} | Temp: {pacote_atual['temperatura']}")
        time.sleep(1)
        print("[CONCLUÍDO] Pacote processado e arquivado.\n")

    print("\n--- INICIANDO UPLINK DE COMANDOS (PILHA) ---")
    historico_comandos = PilhaComandos()

    historico_comandos.empilhar({'id_satelite': 102, 'acao': 'Calibrar Lentes'})
    time.sleep(0.5)
    historico_comandos.empilhar({'id_satelite': 101, 'acao': 'Ajustar Painel Solar'})
    time.sleep(0.5)

    # Comando perigoso
    historico_comandos.empilhar({'id_satelite': 105, 'acao': 'DESLIGAR SISTEMA VITAL'})

    print("\n[!] ALERTA CRÍTICO: Comando incorreto detectado. Acionando reversão (Ctrl+Z)...")
    time.sleep(1.5)

    # Desfaz o último comando
    historico_comandos.desempilhar()

    ultimo_valido = historico_comandos.topo()
    print(f"\nStatus Seguro. Último comando válido no sistema: '{ultimo_valido['acao']}'")

    print("\n--- APLICANDO ORDENAÇÃO (QUICK SORT) ---")
    # Bagunçando de propósito só pra ver o Quick Sort arrumar
    satelites_baguncados = dados_iniciais[::-1]

    time.sleep(1)
    satelites_ordenados = quick_sort_satelites(satelites_baguncados)

    for s in satelites_ordenados:
        print(f"ID: {s['id']} | Nome: {s['nome']}")

    print("\n--- APLICANDO BUSCA BINÁRIA ---")
    id_procurado = 106
    print(f"Procurando na base de dados pelo ID: {id_procurado}...")
    time.sleep(1)

    resultado_busca = busca_binaria(satelites_ordenados, id_procurado)

    if resultado_busca:
        print(
            f"[ENCONTRADO] Sucesso! Satélite localizado: {resultado_busca['nome']} (Status: {resultado_busca['status']})")
    else:
        print("[NÃO ENCONTRADO] O satélite solicitado não existe no catálogo.")

    print("\n--- FIM DO SISTEMA. TODAS AS TAREFAS CONCLUÍDAS! ---")