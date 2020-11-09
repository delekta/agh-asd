# Check if graph is undirected using sets
# In graph Time complexity is complicated to find
# Time complexity: O(E), we pass through edges twice


class Vertex:
    def __init__(self, idx):
        self.idx = idx


def is_undirected(graph):
    edge_set = set()
    for v in graph:
        for neighbour in graph[v]:
            edge_set.add((v, neighbour))

    for v in graph:
        for neighbour in graph[v]:
            if not (neighbour, v) in edge_set:
                return False

    return True


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)

# Adjacency list for 6 vertexes
adjacency_list = {
    v1: [v2, v5],
    v2: [v1],
    v3: [v6],
    v4: [v6, v5],
    v5: [v1, v4, v6],
    v6: [v3, v4, v5],
}

print(is_undirected(adjacency_list))

# off-topic

# ternary conditional operator in python
a = "YES"
b = "NO"
condition = False
print(a) if condition else print(b)

# deleting objects
# In Python, removing a reference (or a name) can be done with the del keyword,
# but if there are other names(references) to the same object that object will not be deleted.
# e.g
# other is test, checking that both refer to the same object
# True
# del test
# You can still print this object using other reference
