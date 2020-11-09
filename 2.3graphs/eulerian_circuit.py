# Eulerian trail is a trail in a finite connected!!! graph that visits every edge exactly once.
# Eulerian cycle is an Eulerian trail that starts and ends on the same vertex.
# WKW all vertex must have even degree( necessary and sufficient condition)


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


def eulerian_cycle(G, stack, pointers, v):
    for u in range(pointers[v], len(G)):
        pointers[v] = u + 1  # jesli tego nie ma złożoność O(n^3), z tym O(n^2)
        if G[v][u] == 1:

            G[v][u] = 0
            G[u][v] = 0
            eulerian_cycle(G, stack, pointers, u)
    stack.push(v)


graph = [
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0],
]

stack = StackA(len(graph) * len(graph))
pointers = [0 for _ in range(len(graph))]


eulerian_cycle(graph, stack, pointers, 6)
while not stack.is_empty():
    print(stack.pop(), "->", end=" ")
