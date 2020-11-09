

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