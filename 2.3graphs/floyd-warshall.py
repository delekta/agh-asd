# floyd-warshall
# Floyd–Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive or negative
# edge weights (but with no negative cycles)


def floyd_warshall(graph):
    costs = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]
    parents = [[-1 for _ in range(len(graph))] for _ in range(len(graph))]
    for v in range(len(graph)):
        for u in range(len(graph)):
            # if we have undirected graph and we want min_cycles, we can omit this if
            if v == u:
                costs[v][u] = 0
            elif graph[v][u] == 0:
                costs[v][u] = float('inf')
            else:
                costs[v][u] = graph[v][u]

    for t in range(len(graph)):
        for v in range(len(graph)):
            for u in range(len(graph)):
                if costs[v][u] > costs[v][t] + costs[t][u]:
                    costs[v][u] = costs[v][t] + costs[t][u]
                    parents[v][u] = t

    return costs, parents


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print("\n")


def print_path(v, u, parents, graph):
    if graph[v][u] != 0:
        return str(v) + str(u)
    t = parents[v][u]
    return print_path(v, t, parents, graph) + print_path(t, u, parents, graph)


graph = [
    [0, 4, 3, 0, 0, 0, 0],
    [4, 0, 0, 0, 3, 20, 0],
    [3, 0, 0, 7, 10, 0, 0],
    [0, 0, 7, 0, 2, 0, 0],
    [0, 3, 10, 2, 0, 0, 5],
    [0, 20, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 5, 5, 0],
]
undirected_graph = [
    [0, 5, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [7, 0, 0, 1, 0],
    [0, 0, 0, 0, 2],
    [0, 2, 2, 0, 0],
]

costs, parents = floyd_warshall(graph)
print(print_matrix(costs))
print(print_path(0, 6, parents, graph))