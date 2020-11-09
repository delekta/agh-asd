# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce.
# Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych
# (które tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac
# pojedynczo a operatorowi dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci
# znajdujacy sie w zasiegu działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny).
# Proszę zaproponować algorytm podający kolejność wyłączania stacji.
# Pomysł: BFS, i  robimy dodatkową kolejke zeby zapamietywac kolejnosc w jakiej elementy wchodziły, pozniej ją odracamy,
# lub tworzymy stos na ktorym zapisujemy elementy w kolejnosci w ktorej wchodza na stos
# Duzo lepszym rozwiazaniem jest DFS, i obcinamy, gdy juz nie ma dzieci


class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.d = None
        self.visited = False


class Node:
    def __init__(self):
        self.next = None
        self.vertex = None


class QueueL:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def put(self, vertex):
        new = Node()
        new.vertex = vertex
        self.tail.next = new
        self.tail = self.tail.next

    def get(self):
        # if we get the only one element
        if self.head.next is self.tail:
            self.tail = self.head

        temp = self.head.next
        self.head.next = temp.next
        return temp.vertex

    def top(self):
        return self.head.next.vertex

    def is_empty(self):
        return self.head.next is None


# head is sentinel node, iterative version
def reverse_queue(head, tail):
    # tail is not used, because, it is variable and in python variable are immutable
    tail = head.next
    current = None
    prev = None
    while head.next is not None:
        current = head.next
        head.next = current.next
        current.next = prev
        prev = current
    head.next = current
    # return head, tail


# tail recursion
def reverse_queue_recursive(head, curr, prev=None):
    if curr.next is None:
        head.next = curr
        curr.next = prev
        return

    temp = curr.next
    curr.next = prev
    reverse_queue_recursive(head, temp, curr)


# normal recursion
def reverse_queue_recursive_normal(head, current):
    if current.next is None:
        return current

    temp = current.next

    head.next = reverse_queue_recursive_normal(head, temp)

    temp.next = current
    # important!!!
    current.next = None
    return head.next


# test functions
def change(x, y):
    x.idx = 88
    y.idx = 99


def change2(a, b):
    a = 88
    b = 99


def BFS(G, s):
    Q = QueueL()
    RES = QueueL()

    for u in G:
        u.d = 0
        u.visited = False

    Q.put(s)
    RES.put(s)
    s.visited = True

    while not Q.is_empty():
        v = Q.get()
        for u in G[v]:
            if not u.visited:
                u.visited = True
                u.d = v.d + 1
                Q.put(u)
                RES.put(u)

    # reverse_queue(RES.head, RES.tail)
    # reverse_queue_recursive(RES.head, RES.head.next)
    reverse_queue_recursive_normal(RES.head, RES.head.next)
    # RES have order in which we should remove vertices
    while not RES.is_empty():
        v = RES.get()
        print(v.idx)


# po wyjsciu z rekurencji obcinasz, dziala
def DFS(G, v):
    v.visited = True
    for u in G[v]:
        if not u.visited:
            DFS(G, u)
    
    print(v.idx)
    del v


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

# BFS(adjacency_list, v1)
DFS(adjacency_list, v1)

x = Vertex(8)
y = Vertex(9)
# Object is changing
change(x, y)
print(x.idx, y.idx)

a = 8
b = 9
# Variable is not changing
change2(a, b)
print(a, b)

# "Pointer is changing", There is no pointers in python so if we change object which have variables potentially
# variables which point to object, change will be visible

