def quick_sort_satelites(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]


    esquerda = [x for x in lista if x['id'] < pivo['id']]
    meio = [x for x in lista if x['id'] == pivo['id']]
    direita = [x for x in lista if x['id'] > pivo['id']]

    return quick_sort_satelites(esquerda) + meio + quick_sort_satelites(direita)


def busca_binaria(lista_ordenada, id_alvo):
    """
    Algoritmo de Busca Binária.
    Procura um satélite pelo ID de forma extremamente rápida.
    OBS: A lista precisa estar ordenada para funcionar!
    """
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        palpite = lista_ordenada[meio]

        if palpite['id'] == id_alvo:
            return palpite

        if palpite['id'] > id_alvo:
            fim = meio - 1
        else:
            inicio = meio + 1

    return None