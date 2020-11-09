
class BST_Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
        self.left_count = 0


class BST_Tree:
    def __init__(self):
        self.root = None

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

    def find(self, key):
        curr = self.root
        while curr is not None:
            if curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def remove(self, key):
        x = self.find(key)
        if x is None:
            return
        # co jesli chcemy usunac roota?
        # - chyba ta operacja jest bez sensu
        if x.left is None and x.right is None:
            if x.parent.key > x.key:
                x.parent.left = None
            else:
                x.parent.right = None
        elif x.left is None or x.right is None:
            parent = x.parent

            if x.left is not None:
                child = x.left
            else:
                child = x.right

            if parent.key > child.key:
                parent.left = child
            else:
                parent.right = child
            child.parent = parent

        # when node has two kids, debugging needed 19.05.2020
        else:
            # easy version, overwrite values
            succ = self.succ(x)
            x.key = succ.key
            x.value = succ.value

            # problem zmiany self.root jak usuwamy roota
            if x is self.root:
                self.root = succ

            # if successor is a right son
            if succ == x.right:
                x.right = succ.right
            else:
                if succ.parent.key > succ.key:
                    succ.parent.left = None
                else:
                    succ.parent.right = None

            return
            # switching indicators

            succ.parent = x.parent
            succ.left = x.left
            succ.right = x.right

            # tez wazne
            if succ.parent.key > key:
                succ.parent.left = succ
            else:
                succ.parent.right = succ

            succ.left.parent = succ
            succ.right.parent = succ

            # redundant
            x.parent = None
            x.left = None
            x.right = None

    def min(self, node):
        root = node
        while root.left is not None:
            root = root.left
        return root

    def max(self, node):
        root = node
        while root.right is not None:
            root = root.right
        return root

    def succ(self, node):
        x = node
        if x.right is not None:
            return self.min(x.right)

        # because there can be successor even though there is no right subtree
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def pred(self, node):
        x = node
        if x.left is not None:
            return self.max(x.left)

        # because there can be predecessor even though there is no left subtree
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def print_rec(self, node):
        if node is None:
            return
        self.print_rec(node.parent)
        print(node.key, end=" ")

    def print_path(self, key):
        x = self.find(key)
        self.print_rec(x)
        print("\n")

    # better if path exist, but if not
    def print_diff(self, key):
        curr = self.root
        while curr is not None:
            print(curr.key, end=" ")
            if curr.key == key:
                break
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        print("\n")

    def inorder_walk(self, root):
        if root is not None:
            self.inorder_walk(root.left)
            print(root.key)
            self.inorder_walk(root.right)

    def kth_smallest(self, root, k):
        if root is None:
            return
        count = root.left_count + 1
        if count == k:
            print(root.key)
        elif k < count:
            self.kth_smallest(root.left, k)
        else:
            self.kth_smallest(root.right, k - count)

    def create_tree(self):
        while True:
            print(" i - insert(key, val) \n r - remove(key) \n p - print_path(key) \n e - end \n w - inorder-walk \n k - find k-th smallest")
            opr = input("Podaj komende:")
            if opr == 'i':
                key1 = int(input("Podaj klucz:"))
                val = input("Podaj wartosc: ")
                self.insert(key1, val)
            elif opr == 'r':
                key2 = int(input("Podaj klucz:"))
                self.remove(key2)
            elif opr == 'p':
                key3 = int(input("Podaj klucz:"))
                self.print_path(key3)
            elif opr == 'w':
                self.inorder_walk(self.root)
            elif opr == 'k':
                k = int(input("Podaj k: "))
                self.kth_smallest(self.root, k)
            elif opr == 'e':
                break
            else:
                print("Komenda ", opr, " nie istnieje")


tree = BST_Tree()
tree.create_tree()



