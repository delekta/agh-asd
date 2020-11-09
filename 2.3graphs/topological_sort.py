# DAG - directed acyclic graph
# ułożenie wierzchołków że pokazują tylko z "lewa do prawa"


class StackA:
    def __init__(self, length):
        self.arr = [None] * length
        self.length = length
        self.size = 0

    def push(self, element):
        self.arr[self.size] = element
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr[self.size]

    def top(self):
        return self.arr[self.size - 1]

    def is_empty(self):
        return self.size == 0


def dfs(G):
    def dfs_visit(G, v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfs_visit(G, u)
        stack.push(v)

    visited = [False for _ in range(len(G))]
    stack = StackA(len(G))
    for v in range(len(G)):
        if not visited[v]:
            dfs_visit(G, v)
    return stack


graph1 = [
    [1, 2],  # edges of vertex 0
    [2, 3],  # edges of vertex 1
    [],  # itd.
    [4, 5, 6],
    [],
    [],
    [],
    [2],
    [1, 7],
    [7, 8],
]

graph2 = [
    [2],
    [],
    [],
    [0],
    [1, 2],
]

stack = dfs(graph2)
while not stack.is_empty():
    print(stack.pop())
