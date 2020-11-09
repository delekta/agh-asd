from queue import PriorityQueue


def relax(v, u, weight, queue, parent, graph):
    if graph[u][0] > graph[v][0] + weight:
        graph[u][0] = graph[v][0] + weight
        parent[u] = v
        queue.put(graph[u])


def dijkstra(graph, s, edges, visited, parent):
    graph[s][0] = 0
    queue = PriorityQueue()
    for v in graph:
        queue.put(v)

    S = []
    while not queue.empty():
        v = queue.get()[1]
        if not visited[v]:
            S.append(v)
            visited[v] = True
            for edge in edges[v]:
                relax(v, edge[0], edge[1], queue, parent, graph)
    print(S)


def print_path(s, t, parent):
    if t == s:
        print(t, end=" ")
        return
    print_path(s, parent[t], parent)
    print(t, end=" ")


length = 7
graph = [[float('inf'), i] for i in range(length)]
visited = [False for _ in range(len(graph))]
parent = [-1 for _ in range(len(graph))]

# edge represented as (target_vertex, val)
edges = [
    [(1, 4), (2, 3)],
    [(5, 20), (4, 3), (0, 4)],
    [(3, 7), (4, 10), (0, 3)],
    [(4, 2), (2, 7)],
    [(2, 10), (1, 3), (3, 2), (6, 5)],
    [(1, 20), (6, 5)],
    [(5, 5), (4, 15)],
]

dijkstra(graph, 0, edges, visited, parent)
print(graph[5][0])
print_path(0, 5, parent)

