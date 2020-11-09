from queue import PriorityQueue


def relax(item, i, queue, parent, graph, dist):
    if dist[i] > dist[item] + graph[item][i]:
        dist[i] = dist[item] + graph[item][i]
        parent[i] = item
        queue.put((dist[i], i))


def dijkstra(graph, s):
    visited = [False for _ in range(len(graph))]
    parent = [-1 for _ in range(len(graph))]
    dist = [float('inf') for _ in range(len(graph))]

    dist[0] = 0
    queue = PriorityQueue()

    queue.put((dist[s], s))
    while not queue.empty():
        item = queue.get()[1]
        if not visited[item]:
            visited[item] = True
            for i in range(len(graph)):
                if graph[item][i] > 0:
                    relax(item, i, queue, parent, graph, dist)
    print(dist)


matrix = [
    [0, 4, 3, 0, 0, 0, 0],
    [4, 0, 0, 0, 3, 20, 0],
    [3, 0, 0, 7, 10, 0, 0],
    [0, 0, 7, 0, 2, 0, 0],
    [0, 3, 10, 2, 0, 0, 5],
    [0, 20, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 5, 5, 0],
]
dijkstra(matrix, 0)
