from collections import deque
# (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V,E). Kierowca chce przejechać z miasta (wierzchołka)
# s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę.
# Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby opłat. W ogólności graf G jest
# skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.

"""
    We  can solve it with dijkstra, but time complexity will be O(E * logV).
    We can also solve it with BFS -> Time complexity: O(V + E)
    BFS solution:
        In normal BFS of a graph all edges have equal weight but in 0-1 BFS some edges may have 0 weight and some may
    have 1 weight. In this we will not use bool array to mark visited nodes but at each step we will check for
    the optimal distance condition. We use double ended queue to store the node. While performing BFS if a edge
    having weight = 0 is found node is pushed at front of double ended queue and if a edge having weight = 1 is
    found, it is pushed at back of double ended queue.
"""


def zero_one_bfs(s, t, graph):
    # Initialize distances from given source
    dist = [float('inf') for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    # double ende queue to do BFS.
    Q = deque()
    dist[s] = 0
    Q.append(s)

    while Q:
        u = Q.popleft()
        if not visited[u]:
            visited[u] = True
            for i in range(len(graph[u])):
                v = graph[u][i][0]
                # checking for the optimal distance
                if dist[v] > dist[u] + graph[u][i][1]:
                    dist[v] = dist[u] + graph[u][i][1]

                    # Put 0 weight edges to front and 1 weight
                    # edges to back so that vertices are processed
                    # in increasing order of weights.
                    if graph[u][i][1] == 0:
                        Q.appendleft(v)
                    else:
                        Q.append(v)

    print(dist)


s = 0
t = 4
# edge (destination vertex, cost)
graph = [
    [(1, 0), (7, 1)],
    [(0, 0), (2, 1), (7, 1)],
    [(1, 1), (3, 0), (5, 0), (8, 1)],
    [(2, 0), (4, 1), (5, 1)],
    [(3, 1), (5, 1)],
    [(3, 1), (4, 1), (6, 1)],
    [(5, 1), (7, 1), (8, 1)],
    [(0, 1), (1, 1), (6, 1), (8, 1)],
    [(2, 1), (6, 1), (7, 1)],
]

zero_one_bfs(s, t, graph)
