# BST tree

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def get_max(self, node):
        while node.right != None:
            node = node.right
        return node.val

    def get_min(self, node):
        while node.left != None:
            node = node.left
        return node.val

    def print_tree(self, node):
        if node != None:
            self.print_tree(node.left)
            print(str(node.val))
            self.print_tree(node.right)



tree = Tree()
tree.insert(-2)
tree.insert(5)
tree.insert(15)
tree.insert(63)
tree.insert(21)
tree.insert(37)
tree.insert(16)

tree.print_tree(tree.root)
print("Max:", tree.get_max(tree.root))
print("Min:", tree.get_min(tree.root))



