#  (sklejanie odcinków) Dany jest ciąg przedziałów postaci [ai,bi]. Dwa przedziały można skleić jeśli mają dokładnie
#  jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
#  1. Problem stwierdzenia, czy da się uzyskąć przedział [a,b] przez sklejanie odcinków.
#  2. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.
#  Pomysł: przekształcamy przedzialy na wierzcholki i sprawdzamy czy mozna przejsc od wierzcholka a do b

class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.visited = False
        self.d = 0  # distance from root


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


# BFS be like
# 1 Problem
def is_possible(G, a, b):
    Q = QueueL()

    Q.put(a)
    a.visited = True

    while not Q.is_empty():
        v = Q.get()
        for u in G[v]:
            if u.idx is b.idx:
                return True
            if not u.visited:
                u.visited = True
                Q.put(u)
    return False


# 2 Problem
# Needed debugging 11.04.2020
def is_possible_k(G, a, b, k):
    Q = QueueL()

    Q.put(a)
    a.visited = True
    a.d = 0

    while not Q.is_empty():
        v = Q.get()
        # Cause if v.d == k, their child have d > k
        if v.d == k:
            break
        for u in G[v]:
            if u is b and u.d <= k - 1:
                return True
            if not u.visited:
                u.d = v.d + 1
                u.visited = True
                Q.put(u)
    return False


arr = [(1, 3), (2, 4), (3, 7), (4, 5), (3, 5), (5, 6), (2, 3)]

# creating adjacency list, cant use for this algorithm cause I cant distinguish vertices
adjacency_list = {}
for el in arr:
    v0 = Vertex(el[0])
    v1 = Vertex(el[1])
    if el[0] in adjacency_list:
        adjacency_list[v0].append(v1)
    else:
        adjacency_list[v0] = [v1]

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

# Adjacency list for 6 vertexes
adjacency_list2 = {
    v1: [v3],
    v2: [v3, v4],
    v3: [v5, v7],
    v4: [v5],
    v5: [v6],
    v6: [],
    v7: [],
}

print(is_possible(adjacency_list2, v1, v7))
print(is_possible_k(adjacency_list2, v1, v7, 10))
