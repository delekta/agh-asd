def reverse_adjacency_list(graph):
    new = [[] for _ in range(len(graph))]
    for v in range(len(graph)):
        for u in graph[v]:
            new[u].append(v)
    return new


def reverse_adjacency_matrix(graph):
    new = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            new[i][j] = graph[j][i]
    return new


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("\n")
    print("========")


adjacency_list = [[1], [3], [0, 1], []]
print(adjacency_list)
print(reverse_adjacency_list(adjacency_list))

adjacency_matrix = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
]
print_matrix(adjacency_matrix)
print_matrix(reverse_adjacency_matrix(adjacency_matrix))


