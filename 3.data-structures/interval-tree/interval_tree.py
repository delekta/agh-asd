# Interval tree


class Node:
    def __init__(self):
        self.intervals = []
        self.key = None
        self.left = Node_Leaf()
        self.right = Node_Leaf()  # ważne, takie node'y od ostatnich punktow
        self.parent = None
        self.Leaf = False
        self.span = [None, None]


class Node_Leaf:
    def __init__(self):
        self.span = [None, None]
        self.intervals = []
        self.Leaf = True


class Interval_Tree:
    def __init__(self):
        self.root = None
        self.left_limit = -float('inf')
        self.right_limit = float('inf')

    def insert_point(self, key):
        x = Node()
        x.key = key
        prev = None
        # if self.root is not None:
        #     print("self root :", self.root.key)
        curr = self.root

        last_greater = self.right_limit
        last_smaller = self.left_limit

        if curr is not None:
            while not curr.Leaf:
                prev = curr

                if curr.key > key:
                    last_greater = curr.key
                    curr = curr.left
                else:
                    last_smaller = curr.key
                    curr = curr.right

        x.span[0] = last_smaller
        x.span[1] = last_greater

        x.parent = prev
        if self.root is None:
            self.root = x
        else:
            if prev.key > key:
                prev.left = x
            else:
                prev.right = x
        # wazne
        x.left.span[0] = x.span[0]
        x.left.span[1] = x.key

        x.right.span[0] = x.key
        x.right.span[1] = x.span[1]

    def _insert_interval(self, curr, l_limit, r_limit):
        if not (curr.span[0] >= l_limit and curr.span[1] <= r_limit):
            if l_limit < curr.key < r_limit:
                self._insert_interval(curr.left, l_limit, curr.key)
                self._insert_interval(curr.right, curr.key, r_limit)
            elif l_limit >= curr.key:
                self._insert_interval(curr.right, l_limit, r_limit)
            elif r_limit <= curr.key:
                self._insert_interval(curr.left, l_limit, r_limit)
        elif curr.span[0] == l_limit and curr.span[1] == r_limit:
            curr.intervals.append((l_limit, r_limit))

    def insert_interval(self, interval):
        l_limit = interval[0]
        r_limit = interval[1]
        curr = self.root
        self._insert_interval(curr, l_limit, r_limit)

    def _remove_interval(self, curr, l_limit, r_limit):
        if not (curr.span[0] >= l_limit and curr.span[1] <= r_limit):
            if l_limit < curr.key < r_limit:
                self._insert_interval(curr.left, l_limit, curr.key)
                self._insert_interval(curr.right, curr.key, r_limit)
            elif l_limit >= curr.key:
                self._insert_interval(curr.right, l_limit, r_limit)
            elif r_limit <= curr.key:
                self._insert_interval(curr.left, l_limit, r_limit)
        elif curr.span[0] == l_limit and curr.span[1] == r_limit:
            curr.intervals.remove((l_limit, r_limit))

    def remove_interval(self, interval):
        l_limit = interval[0]
        r_limit = interval[1]
        root = self.root
        self._remove_interval(root, l_limit, r_limit)

    def query(self, point):
        curr = self.root
        while curr is not None:
            if curr.intervals:
                print(curr.intervals)
            if curr.Leaf:
                break
            elif curr.key > point:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder_walk(self, curr):
        if not curr.Leaf:
            self.inorder_walk(curr.left)
            print(curr.key, ": ", curr.intervals)
            self.inorder_walk(curr.right)
        else:
            print(curr.intervals)

    def create_tree(self):
        while True:
            print("ii - insert_interval(l_limit, r_limit) \nip - insert_point(key) \nq - query(point) \n"
                  "iow - inorder_walk() \ne - zakoncz")
            opr = input("Podaj komende:")
            if opr == 'ii':
                l_limit = int(input("Podaj lewe ograniczenie:"))
                r_limit = int(input("Podaj prawe ograniczenie:"))
                self.insert_interval((l_limit, r_limit))
            elif opr == 'ip':
                key2 = int(input("Podaj klucz:"))
                self.insert_point(key2)
            elif opr == 'q':
                point = int(input("Podaj punkt:"))
                self.query(point)
            elif opr == 'iow':
                root = self.root
                self.inorder_walk(root)
            elif opr == 'e':
                break
            else:
                print("Komenda ", opr, " nie istnieje")
            print("\n")


Tree = Interval_Tree()
Tree.create_tree()




