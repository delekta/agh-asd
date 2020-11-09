# Proszę podać algorytm, który mając na wejściu graf G reprezentowany przez listy sąsiedztwa sprawdza,
# czy dla każdej krawędzie u → v istnieje także krawędź przeciwna. (Czy jest nieskierowany)


# G is a list of list
def is_undirected(G):
    n = len(G)
    # creating adjacency matrix, cause checking if edge exist is O(1)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    counter = 0
    i, j = 0, 0
    while i < n:
        # important
        j = 0
        while j < len(G[i]):
            poz = G[i][j]
            graph[i][poz] = 1
            if graph[poz][i] == 1:
                counter -= 1
            else:
                counter += 1
            j += 1
        i += 1

    # if we add the same amount of edges as we remove it is undirected graph
    print(graph, counter)
    return counter == 0


G = [[1, 2], [0], [0, 3, 4], [2, 5], [2], [5]]
print(is_undirected(G))
