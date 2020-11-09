# Most - krawędz w spojnym grsfie nieskierowanym, której usunięcie spowoduje rozspojnienie grafu
# WKW Krawedz jest mostem, gdy nie lezy na zadnym cyklu prostym


def count_low(G, v, visited, low, parent, res, entry, time=1):

    visited[v] = True
    entry[v] = time
    low[v] = time

    for u in G[v]:
        if not visited[u]:

            parent[u] = v
            time = count_low(G, u, visited, low, parent, res, entry, time + 1)

            low[v] = min(low[v], low[u])

            if entry[v] < low[u]:
                res.append((v, u))

        # ważny warunek
        elif visited[v] and parent[v] != u:

            # krawedz wsteczna
            low[v] = min(low[v], low[u])

    return time


def find_bridges(G):
    visited = [False for _ in range(len(G))]
    low = [float('inf') for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    entry = [-1 for _ in range(len(G))] # tak, poradzimy sobie bez! Ale w punktach artykulacji
                                        # juz sobie bez tego nie poradzisz

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
graph2 = [
    [1],
    [2],
    [3],
    [],
]
graph3 = [
    [1],
    [0, 2, 5],
    [1, 3],
    [2, 4, 5],
    [4],
    [1, 3]
]
find_bridges(graph3)




