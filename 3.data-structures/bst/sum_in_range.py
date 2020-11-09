# (suma kluczy z przedziału) Proszę opisać jak zmodyfikować drzewa czerwono-czarne
# (przechowujące liczby jako klucze) tak, by operacja sum(T, x, y) obliczająca sumę elementów z drzewa T
# o wartościach z przedziału [x, y] działała w czasie O(log n) (gdzie n to liczba węzłów drzewa T). Pozostałe
# operacje na powstałym drzewie powinny miec taka sama złożoność jak w standardowym drzewie czerwonoczarnym.


class BST_Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.left_sum = 0
        self.right_sum = 0


class BST_Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        x = BST_Node(key)
        prev = None
        curr = self.root

        while curr is not None:
            prev = curr
            if curr.key > key:
                curr.left_sum += key  # needed for sum
                curr = curr.left
            else:
                curr.right_sum += key
                curr = curr.right

        x.parent = prev
        if self.root is None:
            self.root = x
        else:
            if prev.key > key:
                prev.left = x
            else:
                prev.right = x

    def sum_in_range(self, x, y):
        shared_root = self.root
        currX = self.root
        currY = self.root

        # finding shared root
        while not (currX.key == x and currY.key == y):
            if currX is currY:
                shared_root = currX

            if currX.key != x:
                if x < currX.key:
                    currX = currX.left
                else:
                    currX = currX.right

            if currY.key != y:
                if y < currY.key:
                    currY = currY.left
                else:
                    currY = currY.right

        sum = 0
        sum_it = True

        while currX is not shared_root:
            if sum_it:
                sum += currX.key
                sum += currX.right_sum
            if currX is currX.parent.left:
                sum_it = True
            else:
                sum_it = False
            currX = currX.parent

        sum_it = True

        while currY is not shared_root:
            if sum_it:
                sum += currY.key
                sum += currY.left_sum
            if currY is currY.parent.right:
                sum_it = True
            else:
                sum_it = False
            currY = currY.parent

        sum += shared_root.key

        return sum

    def create_tree(self):
        while True:
            print(" i - insert(key, val) \n s - (sum_value) \n e - (end)")
            opr = input("Podaj komende:")
            if opr == 'i':
                key1 = int(input("Podaj klucz:"))
                self.insert(key1)
            elif opr == "s":
                x = int(input("Podaj x: "))
                y = int(input("Podaj y: "))
                print(self.sum_in_range(x, y))
            elif opr == "e":
                break
            else:
                print("Komenda ", opr, " nie istnieje")


T = BST_Tree()
T.create_tree()