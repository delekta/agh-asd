# Mowimy ze u i v naleza do tej samej silnie spojnej skladowej jesli
# istnieja skierowane sciezki z u do v i z v do u
# Zrob wersje z lista adjacencji  27.04.2020
# 1. Collect times of processed
# 2. Reverse edges
# 3. For every vertex call dfs to color vertices in the same component( iterating from the greatest times of processing)


# reversing edges
def get_transposed_matrix(graph):
    new = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            new[i][j] = graph[j][i]
    return new


def get_transposed_list(graph):
    new = [[] for _ in range(len(graph))]
    for v in range(len(graph)):
        for u in graph[v]:
            new[u].append(v)
    return new


def partition(arr, left, right):
    pivot = arr[right][1]
    i = left - 1
    for j in range(left, right):
        if arr[j][1] > pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q + 1, right)


def strongly_connected_component_for_adjacency_matrix(G):
    def dfs_processed(G, v, time=0):
        visited[v] = True
        for u in range(pointers[v], len(G)):
            pointers[v] = u + 1
            if G[v][u] == 1:
                if not visited[u]:
                    time = dfs_processed(G, u, time)
        time += 1
        processed[v] = (v, time)
        return time

    def dfs_component(G, v, c):
        visited[v] = True
        components[v] = c
        for u in range(pointers[v], len(G)):
            pointers[v] = u + 1     # very important, without it recursion depth is exceeded
            if G[v][u] == 1:
                if not visited[u]:
                    dfs_component(G, u, c)

    processed = [-1 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    pointers = [0 for _ in range(len(G))]

    for v in range(len(G)):
        if not visited[v]:
            dfs_processed(G, v)

        G = get_transposed_matrix(G)

    components = [-1 for _ in range(len(G))]
    c = 1

    for i in range(len(G)):
        visited[i] = False
        pointers[i] = 0

    # print(processed)
    quicksort(processed, 0, len(processed) - 1)
    # print(processed)

    # must be sorted decreasing processed time
    for vertex, time in processed:
        if not visited[vertex]:
            dfs_component(G, vertex, c)
            c += 1

    print(components)


def strongly_connected_component_for_adjacency_list(G):
    def dfs_processed(G, v, time=0):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                time = dfs_processed(G, u, time)
        time += 1
        processed[v] = (v, time)
        return time

    def dfs_component(G, v, c):
        visited[v] = True
        components[v] = c
        for u in G[v]:
            if not visited[u]:
                dfs_component(G, u, c)

    processed = [-1 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    for v in range(len(G)):
        if not visited[v]:
            dfs_processed(G, v)

    G = get_transposed_list(G)

    components = [-1 for _ in range(len(G))]
    c = 1

    for i in range(len(G)):
        visited[i] = False

    # print(processed)
    quicksort(processed, 0, len(processed) - 1)
    # print(processed)

    # must be sorted decreasing processed time
    for vertex, time in processed:
        if not visited[vertex]:
            dfs_component(G, vertex, c)
            c += 1

    print(components)


graph = [
  #  0  1  2  3  4  5  6  7  8  9  10
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 0
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 10
]

graph2 = [
    [1, 10],    # 0
    [2, 3],     # 1
    [0],        # 2
    [5],        # 3
    [3, 6],     # 4
    [4],        # 5
    [5],        # 6
    [4, 10],    # 7
    [7],        # 8
    [6, 8],     # 9
    [9],        # 10
]

graph3 = [
    [1, 6],
    [0, 2],
    [3],
    [4],
    [5],
    [3],
    [7],
    [6],
]

strongly_connected_component_for_adjacency_matrix(graph)
strongly_connected_component_for_adjacency_list(graph2)
strongly_connected_component_for_adjacency_list(graph3)
