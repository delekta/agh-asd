# wierzcholek jest punktem artykulacji, jesli jego usuniecie zwieksza liczbe spojnych skladowych
# Wierzchołek jest punktem artykulacji:
# 1. jest korzeniem i ma wiecej niz jednego syna
# 2. nie jest korzeniem, a dla przynajmniej jednego syna low(syna) >= low(v)


def count_low(G, v, visited, low, parent, res, entry, time=1):

    children = 0
    visited[v] = True
    entry[v] = time
    low[v] = time

    for u in G[v]:
        if not visited[u]:

            parent[u] = v
            children += 1
            time = count_low(G, u, visited, low, parent, res, entry, time + 1)

            low[v] = min(low[v], low[u])

            # 1. Case, jest potrzebny
            if parent[v] == -1 and children > 1:
                # print("Case1: ", v)
                res.append(v)

            # 2. Case, musi byc entry[v] <= low[u], Najwazniejszy warunek!!!
            if parent[v] != -1 and entry[v] <= low[u]:
                # print("Case2: ", v)
                res.append(v)

        # ważny warunek
        elif visited[v] and parent[v] != u:

            # krawedz wsteczna
            low[v] = min(low[v], low[u])

    return time


def find_articulation_points(G):
    visited = [False for _ in range(len(G))]
    low = [float('inf') for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    entry = [-1 for _ in range(len(G))]  # musi byc!!!

    res = []
    count_low(G, 0, visited, low, parent, res, entry)
    print(res)


graph = [
    [1, 6],
    [0, 2],
    [1, 3, 6],
    [2, 4, 5],
    [3, 5],
    [3, 4],
    [0, 2, 7],
    [6],
]
# tree, checking Case 1
graph2 = [
    [1, 2],
    [0, 4, 5],
    [0, 3],
    [2],
    [1],
    [1],
]
graph3 = [
    [1, 4],
    [0, 2, 3, 4],
    [1, 3],
    [1, 2],
    [0, 1],
]
find_articulation_points(graph3)
