# In place algorithm for summing values in binary tree(without recursion)

class BST_Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
        self.left_count = 0
        self.visited = False


class BST_Tree:
    def __init__(self):
        self.root = None
        self.rotations = 0

    def insert(self, key, val):
        x = BST_Node(key, val)
        prev = None
        if self.root is not None:
            print("self root :", self.root.key)
        curr = self.root

        while curr is not None:
            prev = curr
            if curr.key > key:
                curr.left_count += 1  # needed for kth_smallest
                curr = curr.left
            else:
                curr = curr.right

        x.parent = prev
        if self.root is None:
            self.root = x
        else:
            if prev.key > key:
                prev.left = x
            else:
                prev.right = x

    def rotate(self, node, sum):
        if not node.visited:
            sum += node.key
            node.visited = True
        if node == self.root:
            self.rotations += 1

        left = node.left
        right = node.right
        parent = node.parent

        node.left = right
        node.right = parent
        node.parent = left

        return sum

    def sum_value(self):
        sum = 0
        curr = self.root
        while self.rotations < 3:
            temp = curr
            if curr.left is not None:
                curr = curr.left
                sum = self.rotate(temp, sum)
            else:
                sum = self.rotate(temp, sum)
        return sum

    def create_tree(self):
        while True:
            print(" i - insert(key, val) \n s - (sum_value) \n e - (end)")
            opr = input("Podaj komende:")
            if opr == 'i':
                key1 = int(input("Podaj klucz:"))
                val = input("Podaj wartosc: ")
                self.insert(key1, val)
            elif opr == "s":
                sum = self.sum_value()
                print(sum)
            elif opr == "e":
                break
            else:
                print("Komenda ", opr, " nie istnieje")

T = BST_Tree()
T.create_tree()