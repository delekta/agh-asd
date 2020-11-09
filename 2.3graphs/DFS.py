# Depth First Search
class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.entry = None
        self.processed = None
        self.visited = False
        self.parent = None


# Time complexity:
# -> O(V + E) using adjacency list
# -> O(V^2)   using adjacency matrix
def DFS(G):
    # inner function
    def DFSvisit(v, time):
        time += 1
        v.entry = time
        v.visited = True
        for u in G[v]:
            if not u.visited:
                u.parent = v
                time = DFSvisit(u, time)
        time += 1
        v.processed = time
        return time

    time = 0
    for v in G:
        v.parent = None
        v.visited = False

    for v in G:
        if not v.visited:
            # we must return time, because variable in python are passed by assignment
            time = DFSvisit(v, time)


# you change time obly when you enter or exit vertex
def connected_DFS(graph, v, time=0):
    time += 1
    v.visited = True
    v.entry = time
    for u in graph[v]:
        if not u.visited:
            u.parent = v
            time = connected_DFS(graph, u, time)
    time += 1
    v.processed = time
    return time


# print path from v1 to vertex:
# do DFS on v1, then call func print_path
def print_path(vertex):
    if vertex is None:
        return
    print_path(vertex.parent)
    print(vertex.idx)


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
    v4: [v5, v6],
    v5: [v1, v4, v6],
    v6: [v3, v4, v5],
}

DFS(adjacency_list)

for v in adjacency_list:
    print("entry: ", v.entry, "processed: ", v.processed)


for v in adjacency_list:
    v.parent = None
    v.visited = False

# printing path
connected_DFS(adjacency_list, v1)
print_path(v3)














