# Kodowanie huffamana


class QueueA:
    def __init__(self, length):
        self.arr = [None] * length
        self.length = length
        self.head = 0
        self.size = 0

    def put(self, val):
        idx = (self.head + self.size) % self.length
        self.size += 1
        self.arr[idx] = val

    def get(self):
        res = self.arr[self.head]
        self.head = (self.head + 1) % self.length
        self.size -= 1
        return res

    def top(self):
        return self.arr[self.head]

    def is_empty(self):
        return self.size == 0


class Leaf:
    def __init__(self, name, count):
        self.name = str(name)
        self.c = count
        self.leftChild = None
        self.rightChild = None
        self.bits = 0


def merge_leafs(leaf1, leaf2):
    name = str(leaf1.name) + str(leaf2.name)
    count = leaf1.c + leaf2.c

    newLeaf = Leaf(name, count)

    # print("leaf1:", leaf1.name, "leaf2:", leaf2.name)
    newLeaf.rightChild = leaf1
    newLeaf.leftChild = leaf2

    return newLeaf


def heapify_min(arr, length, root):
    left = 2 * root + 1
    right = 2 * root + 2
    mini = root
    if left < length and arr[left].c < arr[mini].c:
        mini = left
    if right < length and arr[right].c < arr[mini].c:
        mini = right
    if mini != root:
        arr[root], arr[mini] = arr[mini], arr[root]
        heapify_min(arr, length, mini)


def build_heap(arr, length):
    for i in range((length // 2) - 1, -1, -1):
        # prepering min heap
        heapify_min(arr, length, i)


def heap_sort(arr):
    length = len(arr)
    build_heap(arr, length)
    j = length - 1
    while j > 1:
        arr[j], arr[0], = arr[0], arr[j]
        leaf1 = arr[j]
        heapify_min(arr, j, 0)
        j -= 1
        arr[j], arr[0], = arr[0], arr[j]
        leaf2 = arr[j]
        merged_leaf = merge_leafs(leaf1, leaf2)
        # we add new leaf to an array
        arr[j] = merged_leaf
        #  j += 1 chyba niepotrzebne

        heapify_min(arr, j + 1, 0)
    if j == 1:
        # print("root")
        root = merge_leafs(arr[0], arr[1])
        return root


# get list of tuples (char, count) -> creates leafs
def creates_leafs(arr):
    leafs = []
    # el is a tuple
    for el in arr:
        leaf = Leaf(el[0], el[1])
        leafs.append(leaf)
    return leafs


def huffman_code(arr):
    leafs = creates_leafs(arr)
    return heap_sort(leafs)


def how_many_chars(root, length):
    chars = []
    Q = QueueA(length)
    Q.put(root)
    while not Q.is_empty():
        node = Q.get()
        if node.leftChild is not None and node.rightChild is not None:
            node.leftChild.bits = node.bits + 1
            node.rightChild.bits = node.bits + 1
            Q.put(node.leftChild)
            Q.put(node.rightChild)
        else:
            chars.append((node.name, node.bits))
    return chars


def num_of_bits(root, top=0,sum=0):
    if root.leftChild is None or root.rightChild is None:
        sum += top * root.c
        return sum
    return num_of_bits(root.leftChild, top + 1, sum) + num_of_bits(root.rightChild, top + 1, sum)


arr = [("A", 3), ("B", 5), ("C", 6), ("D", 4), ("E", 2)]
arr2 = [("A", 200), ("B", 700), ("C", 180), ("D", 120), ("E", 70), ("F", 30)]

root = huffman_code(arr2)
print(num_of_bits(root))
print(how_many_chars(root, len(arr2)))


