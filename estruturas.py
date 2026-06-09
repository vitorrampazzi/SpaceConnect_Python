class NoSatelite:

    def __init__(self, satelite):
        self.dado = satelite  # Dicionário com os dados do satélite
        self.proximo = None  # Aponta para o próximo nó na lista


class ListaLigadaSatelites:

    def __init__(self):
        self.cabeca = None

    def adicionar(self, satelite):
        """Adiciona um novo satélite no final da lista."""
        novo_no = NoSatelite(satelite)
        if self.cabeca is None:
            self.cabeca = novo_no
            return

        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def exibir_todos(self):
        if self.cabeca is None:
            print("Nenhum satélite no catálogo orbital.")
            return

        atual = self.cabeca
        print("\n--- CATÁLOGO ORBITAL (Lista Ligada) ---")
        while atual:
            s = atual.dado
            print(
                f"[{s['id']}] {s['nome']} | Agência: {s['agencia']} | Alt: {s['altitude_km']}km | Status: {s['status']}")
            atual = atual.proximo
        print("---------------------------------------\n")


class FilaTelemetria:

    def __init__(self):
        self.pacotes = []

    def enfileirar(self, pacote):

        self.pacotes.append(pacote)
        print(f"[SINAL CAPTADO] Pacote do satélite ID {pacote['id_satelite']} entrou na fila.")

    def desenfileirar(self):

        if self.esta_vazia():
            print("[ALERTA] A fila de telemetria está vazia.")
            return None
        return self.pacotes.pop(0)

    def esta_vazia(self):

        return len(self.pacotes) == 0

    def tamanho(self):
        return len(self.pacotes)


class PilhaComandos:

    def __init__(self):
        self.comandos = []

    def empilhar(self, comando):
        self.comandos.append(comando)
        print(f"[UPLINK] Comando enviado e empilhado: '{comando['acao']}' para Satélite {comando['id_satelite']}")

    def desempilhar(self):
        if self.esta_vazia():
            print("[ALERTA] Nenhum comando no histórico para desfazer.")
            return None
        comando_desfeito = self.comandos.pop()
        print(
            f"[DESFAZER] Comando CANCELADO: '{comando_desfeito['acao']}' (Satélite {comando_desfeito['id_satelite']})")
        return comando_desfeito

    def topo(self):
        if self.esta_vazia():
            return None
        return self.comandos[-1]

    def esta_vazia(self):
        return len(self.comandos) == 0