# SpaceConnect: Rastreamento Orbital e Telemetria

**Global Solution 2026 - 1º Semestre**

## Integrantes do Grupo
* Vitor Rampazzi Franco - RM: 562270
* Daniel Brito - RM: 566236
* Gustavo Borsato - RM: 564621

## Tema Escolhido
Rastreamento orbital e comportamento de satélites.

## Descrição do Projeto e Objetivo da Solução
O SpaceConnect é uma aplicação backend em Python desenvolvida para simular e gerenciar o monitoramento de satélites em órbita. 
O objetivo principal é demonstrar o uso prático de Estruturas de Dados e Algoritmos no processamento de sinais de telemetria, manutenção de um catálogo orbital atualizado e controle seguro de comandos enviados aos satélites.

## Fonte dos Dados Utilizados
Os dados foram estruturados em um arquivo `satelites_data.csv`, simulando bases de dados de agências espaciais reais (como SpaceX, NASA e INPE) que contêm identificadores, nomes, altitudes e status operacional dos equipamentos.

## Estruturas de Dados Implementadas
* **Lista Ligada Simples:** Utilizada para manter o Catálogo Orbital principal em memória, permitindo o armazenamento de objetos formatados em nós.
* **Fila (Queue - FIFO):** Implementada para a simulação do recebimento e processamento sequencial de pacotes de telemetria enviados pelos satélites.
* **Pilha (Stack - LIFO):** Utilizada como um Histórico de Comandos (Uplink), viabilizando a função "Desfazer" para reverter o último comando crítico enviado por engano.

## Algoritmos Utilizados
* **Ordenação (Quick Sort):** Responsável por ordenar eficientemente o catálogo bagunçado de satélites com base em seus IDs principais.
* **Busca (Busca Binária):** Aplicado sobre a lista após a ordenação, permitindo localizar rapidamente satélites no catálogo com complexidade O(log n).

## Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python 3.x
* **Bibliotecas Embutidas:** `csv` (leitura da base de dados) e `time` (simulação de delay e operações em tempo real).

## Explicação do Funcionamento
O sistema inicia carregando o CSV na memória e populando uma Lista Ligada. Em seguida, a aplicação simula o fluxo em tempo real:
1. Recebe pacotes de sinais na fila e processa-os com tempo de simulação.
2. Simula o envio manual de comandos para os satélites usando uma Pilha, exibindo a reversão da última ação antes que um desastre ocorra.
3. Demonstra a organização do código aplicando um Quick Sort na estrutura base e efetuando uma Busca Binária bem-sucedida por um satélite específico.

## Instruções de Execução
1. Certifique-se de ter o Python 3.x instalado na sua máquina.
2. Clone este repositório.
3. Garanta que os arquivos `main.py`, `estruturas.py`, `algoritmos.py` e `satelites_data.csv` estejam localizados no mesmo diretório.
4. Pelo terminal ou prompt de comando, navegue até a pasta do projeto e execute:
   ```bash
   python main.py
