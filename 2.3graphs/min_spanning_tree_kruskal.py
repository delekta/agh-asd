# kruskal's algorithm


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


# find / union
def make_set(id):
    x = Node(id)
    return x


def find(x):
    if x.parent is not x:
        x.parent = find(x.parent)
    # must be x.parent !!!(not x, if we return x we do not compress)
    return x.parent


def union(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(edge_list, num_of_vertices):
    # sort by third element in tuple
    edge_list.sort(key=lambda x: x[2])
    vertices = [make_set(i) for i in range(num_of_vertices)]

    res = []
    for edge in edge_list:
        x = find(vertices[edge[0]])
        y = find(vertices[edge[1]])
        if x is not y:
            res.append(edge)
            union(x, y)
    return res


# representing [vertex1, vertex2, val]
edge_list = [(0, 1, 3), (1, 2,  7), (2, 3, 5), (3, 5, 10), (2, 5, 12), (4, 5, 17),
             (1, 4, 1), (1, 6, 12), (0, 6, 4), (4, 6, 3), (4, 7, 5)]

num_of_vertices = 8
min_tree = kruskal(edge_list, num_of_vertices)
print(min_tree)



