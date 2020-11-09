# Breadth First Search
class Vertex:
    def __init__(self, val):
        self.val = val
        self.d = None
        self.visited = None
        self.parent = None


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


# we start with adjacency list
def BFS(G, s):
    Q = QueueL()

    for vertex in G:
        vertex.visited = False
        vertex.parent = None
        vertex.d = 0

    Q.put(s)
    s.visited = True

    while not Q.is_empty():
        v = Q.get()
        for u in G[v]:
            if not u.visited:
                u.visited = True
                u.d = v.d + 1
                u.parent = v
                Q.put(u)


# works if you do BFS('src') before
def print_path_from_src_to_dest(src, dest):
    temp = dest
    RES = StackA(10)
    for _ in range(dest.d + 1):
        RES.push(temp.val)
        temp = temp.parent

    while not RES.is_empty():
        print(RES.pop(), end=" ")


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

BFS(adjacency_list, v1)
# distance from v1
for v in adjacency_list:
    print(v.val, v.d)

src = v1
dest = v3
print("Path from", src.val, "to", dest.val)
print_path_from_src_to_dest(src, dest)
