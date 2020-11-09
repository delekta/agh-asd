# Sprawdzanie czy graf nieskierowany posiada cykl.


class Vertex:
    def __init__(self, idx):
        self.visited = None
        self.parent = None
        self.idx = idx


class Vertex2:
    def __init__(self,idx):
        self.color = None
        self.idx = idx


class Node:
    def __init__(self):
        self.next = None
        self.val = None


class QueueL:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def put(self, val):
        new = Node()
        new.val = val
        self.tail.next = new
        self.tail = self.tail.next

    def get(self):
        # if we get the only one element
        if self.head.next is self.tail:
            self.tail = self.head

        temp = self.head.next
        self.head.next = temp.next
        return temp.val

    def top(self):
        return self.head.next.val

    def is_empty(self):
        return self.head.next is None


def has_cycle(G, s):
    Q = QueueL()

    for u in G:
        u.visited = None
        u.parent = None

    Q.put(s)
    # important !!!
    s.visited = True

    while not Q.is_empty():
        v = Q.get()
        for u in G[v]:
            if u.visited is None:
                u.visited = True
                u.parent = v
                Q.put(u)
            # if we want to reach vertex which we visited and
            # is differ from parent it means -> Graph has cycle
            elif u.visited and v.parent != u:
                return True
    return False


# Bonus: cykl w grafie nieskierowanym
# Pomysł: jesli bedziemy chcieli jeszcze raz wejsc do SZAREGO wierzcholka to mamy cykl
# DFS algorithm, default color is WHITE, when we process vertex is GRAY, when we end is BLACK
def DFS(graph, vertex):
    vertex.color = "gray"
    is_cycle = False
    for v in graph[vertex]:
        if v.color == "white":
            v.color = "gray"
            is_cycle = is_cycle or DFS(graph, v)
        elif v.color == "gray":
            is_cycle = True
    vertex.color = "black"  # vertex become black, when all of his children is processed, so if we try reach gray
    return is_cycle         # vertex it means that graph has cycle


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

print(has_cycle(adjacency_list, v1))
