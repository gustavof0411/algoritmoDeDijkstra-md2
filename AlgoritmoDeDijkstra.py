# Matemática Discreta 2 - Aluno: Gustavo de França Silva

import networkx as nx
import matplotlib.pyplot as plt


def algoritmoDeDijkstra(grafo, fonte):

    distancias = {vertice: float('inf') for vertice in grafo}
    predecessores = {vertice: 'und' for vertice in grafo}

    # Lista de vértices
    Q = [vertice for vertice in grafo]

    distancias[fonte] = 0
    predecessores[fonte] = fonte

    while (len(Q) > 0):
        # Selecionando o vértice de menor distância
        selecao = float('inf')
        for vertice in Q:
            if distancias[vertice] < selecao:
                selecao = distancias[vertice]
                verticeAtual = vertice

        Q.remove(verticeAtual)

        for vizinho, peso in grafo[verticeAtual].items():

            outraDistancia = distancias[verticeAtual] + peso

            if outraDistancia < distancias[vizinho]:
                distancias[vizinho] = outraDistancia
                predecessores[vizinho] = verticeAtual

    return distancias, predecessores


def caminhoMinimo(fonte, vertice):

    caminhoMaisOtimizado = []
    caminhoMaisOtimizado.append(vertice)

    predecessor = predecessores[vertice]
    caminhoMaisOtimizado.append(predecessor)

    while (predecessor != fonte):
        predecessor = predecessores[predecessor]
        caminhoMaisOtimizado.append(predecessor)

    return sorted(caminhoMaisOtimizado, reverse=True)


def plotagemDeGrafo(grafo):
    grafoPlot = nx.Graph(grafo)

    for vertice in grafo:
        for vizinho, peso in grafo[vertice].items():
            grafoPlot.add_edge(vertice, vizinho, weight=peso)

    maneiraDePlotagem = nx.circular_layout(grafoPlot)

    # Vértices
    nx.draw_networkx_nodes(grafoPlot, maneiraDePlotagem)
    nx.draw_networkx_labels(grafoPlot, maneiraDePlotagem)
    nx.draw_networkx_edges(grafoPlot, maneiraDePlotagem)
    edgeLabels = nx.get_edge_attributes(grafoPlot, "weight")
    nx.draw_networkx_edge_labels(grafoPlot, maneiraDePlotagem, edgeLabels)
    plt.title("Algoritmo de Djikstra - Atividade")
    plt.show()


grafo = {'A': {'B': 1, 'C': 4},
         'B': {'A': 1, 'C': 1, 'D': 3, 'E': 5},
         'C': {'A': 4, 'B': 1, 'D': 2, 'E': 3},
         'D': {'B': 3, 'C': 2, 'E': 2},
         'E': {'B': 5, 'C': 3, 'D': 2}
         }

# Execução

distancias, predecessores = algoritmoDeDijkstra(grafo, 'A')
print("As distâncias são: " + str(distancias) + "\n")
print("Os predecessores são: " + str(predecessores) + "\n")
print("O menor caminho da fonte \'A\' até o vértice \'E\' é " +
      str(caminhoMinimo('A', 'E')))
plotagemDeGrafo(grafo)
