#  Zadanie 1.Proszę zaimplementować funkcję heavy path(T),która na wejściu otrzymuje drzewo T z ważonymi krawędziami
#  (wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę)
#  najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:


class Node:
        def __init__(self):
            self.children = 0  # liczba dzieci węzła
            self.child = []  # lista par (dziecko, waga krawędzi) ... # wolno dopisać własne pola
            self.visited = False
            self.heaviest_path1 = 0
            self.heaviest_path2 = 0


class Max:
    def __init__(self):
        self.max_path = 0


def heavy_path(v):
    def fill_in_heaviest_paths(v):
        v.visited = False
        for child, cost in v.child:
            if not child.visited:
                fill_in_heaviest_paths(child)

        if v.child:  # list is not empty
            for child, cost in v.child:

                if child.heaviest_path1 + cost > v.heaviest_path1:
                    v.heaviest_path2 = v.heaviest_path1  # really important
                    v.heaviest_path1 = child.heaviest_path1 + cost

                elif child.heaviest_path1 + cost > v.heaviest_path2:  # heaviest_path1 !!!
                    v.heaviest_path2 = child.heaviest_path1 + cost

            if v.heaviest_path1 + v.heaviest_path2 > res.max_path:
                res.max_path = v.heaviest_path1 + v.heaviest_path2

    res = Max()
    fill_in_heaviest_paths(v)
    return res.max_path


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()
H = Node()
I = Node()
A.children = 2
A.child = [(B, 5), (C, -1)]
B.child = [(D, -70), (E, 5), (F, 4)]
D.child = [(G, 4), (H, 52)]
H.child = [(I, 1)]

print(heavy_path(A))

