# Prim's algorithm
# Time complexity: O(E*logV)
from queue import PriorityQueue


def relax(v, u, weight, queue, parent, graph):
    if graph[u][0] > weight:
        # important!!!
        graph[u][0] = weight
        parent[u] = v
        queue.put(graph[u])


# ala dijkstra
def prim(graph, edges, visited, parent):
    # dont set distance[0] = 0
    queue = PriorityQueue()
    for v in graph:
        queue.put(v)

    while not queue.empty():
        v = queue.get()[1]
        if not visited[v]:
            visited[v] = True
            for edge in edges[v]:
                relax(v, edge[0], edge[1], queue, parent, graph)
    res = []
    for i in range(len(graph)):
        res.append((i, parent[i]))
    return res




length = 7
length2 = 8
graph = [[float('inf'), i] for i in range(length2)]
visited = [False for _ in range(len(graph))]
parent = [-1 for _ in range(len(graph))]

# represented as (destination_vertex, val)
edges = [
    [(1, 4), (2, 3)],
    [(5, 20), (4, 3), (0, 4)],
    [(3, -2), (4, 10), (0, 3)],
    [(4, -1), (2, 7)],
    [(2, 10), (1, 3), (3, 2), (6, 5)],
    [(1, 20), (6, 5)],
    [(5, 5), (4, 15)],
]
edges2 = [
    [(1, 3), (6, 4)],
    [(0, 3), (4, 1), (2, 7)],
    [(1, 7), (5, 12), (3, 5)],
    [(2, 5), (5, 10)],
    [(1, 1), (5, 17), (6, 3), (7, 5)],
    [(2, 12), (3, 10), (4, 17)],
    [(0, 4), (1, 12), (4, 3)],
    [(4, 5)],
]
print(prim(graph, edges2, visited, parent))
