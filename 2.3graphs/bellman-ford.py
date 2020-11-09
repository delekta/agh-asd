# bellman-ford algorithm


def relax(v, u, weight, parent, graph):
    if graph[u][0] > graph[v][0] + weight:
        graph[u][0] = graph[v][0] + weight
        parent[u] = v


def bellman_ford(graph, s, edges, parent):
    graph[s][0] = 0
    for i in range(len(graph) - 1):
        # iterating over the edges(relax all edges |V| - 1 times)
        for v in range(len(graph)):
            for edge in edges[v]:
                relax(v, edge[0], edge[1], parent, graph)

    # for each edge
    for v in range(len(graph)):
        for edge in edges[v]:
            if graph[edge[0]][0] > graph[v][0] + edge[1]:
                return False
    return True


def print_path(s, t, parent):
    if t == s:
        print(t, end=" ")
        return
    print_path(s, parent[t], parent)
    print(t, end=" ")


length = 7
graph = [[float('inf'), i] for i in range(length)]
parent = [-1 for _ in range(len(graph))]

# edge represented as (target_vertex, val)
edges = [
    [(1, 4), (2, 3)],
    [(5, 20), (4, 3), (0, 4)],
    [(3, -2), (4, 1), (0, 3)],
    [(4, 1)],
    [(2, 1), (1, 3), (3, 2), (6, 5)],
    [(1, 20), (6, 5)],
    [(5, 5), (4, 5)],
]
s = 6
if bellman_ford(graph, s, edges, parent):
    t = 3
    print(graph[t][0])
    print_path(s, t, parent)
else:
    print("negative cycle")
