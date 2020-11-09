#  Sprawdzanie czy graf nieskierowany jest dwudzielny (czyli czy da się podzielić jego wierzchołki na dwa zbiory,
#  takie że krawędzie łączą jedynie wierzchołki z różnych zbiorów).


class Vertex:
    def __init__(self):
        self.color = None


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


# works only for connected graph, we can add to start from all vertices(new wrap function, like in DFS)
# to work for disconnected graphs
# BFS algorithm
def is_bipartite(G, s):
    Q = QueueL()

    for u in G:
        u.color = None

    Q.put(s)
    s.color = 1

    while not Q.is_empty():
        v = Q.get()
        for u in G[v]:
            if u.color is None:
                u.color = 1 - v.color
                Q.put(u)
            elif u.color == v.color:
                return False

    return True


# DFS algorithm
def is_bipartite2(G):
    def is_bipartite_visit(G, v, c):
        for u in G[v]:
            if u.color is None:
                u.color = c
                if not is_bipartite_visit(G, u, 1 - c):
                    return False
            elif u.color == v.color:
                return False
        return True

    for v in G:
        v.color = None

    for v in G:
        if v.color is None:
            if not is_bipartite_visit(G, v, 1):
                return False
    return True


v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()

# Adjacency list for 6 vertexes
adjacency_list = {
    v1: [v2, v5],
    v2: [v1],
    v3: [v6],
    v4: [v5, v6],
    v5: [v1, v4, v6],
    v6: [v3, v4, v5],
}

print(is_bipartite(adjacency_list, v1))
print(is_bipartite2(adjacency_list))
