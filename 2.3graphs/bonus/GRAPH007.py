# Dane jest nieskierowane drzewo, w postaci list
# adjacencji. Do zadanego drzewa zadajemy serię
# zapytań postaci i, j, gdzie i oraz j oznaczają indeksy
# wierzchołków.
# Dla każdego zapytania chcemy informację, czy
# znajdują się na jednej ścieżce od roota, do jakiegoś
# liścia. Root jest dany. Przeprowadź liniowy (O(V + E))
# preprocessing grafu, tak aby dało się na każde z
# zapytań odpowiedzieć w czasie O(1)
# If we preprocessed and for each vertex collect his entry and processed time, we can answer in O(1)
# If j timestamps are inside i timestamps it means that j and i are at the same path from root(j is a child of i)

# Rozwiązanie: Przeprowadzamy klasyczny DFS z dodaniem znaczników czasowych, zaczynając od
# wyróżnionego roota. Jeżeli czas wejścia wierzchołka i jest mniejszy, od czasu wejścia wierzchołka j, a
# jego czas wyjścia jest większy od czasu wejścia wierzchołka j, to j znajduje się w poddrzewie o roocie
# i. Czyli istnieje ścieżka. Jest to WKW. I odpowiedź na pytanie dokonuje się w O(1), ponieważ to tylko
# porównanie liczb.


class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.entry = None
        self.processed = None
        self.visited = None
        self.parent = None


# Time complexity:
# -> O(V + E) using adjacency list
# -> O(V^2)   using adjacency matrix
def DFS(G):
    # inner function
    def DFSvisit(v, time):
        time += 1
        v.entry = time
        v.visited = True
        for u in G[v]:
            if not u.visited:
                u.parent = v
                time = DFSvisit(u, time)
        time += 1
        v.processed = time
        return time

    time = 0
    for v in G:
        v.parent = None
        v. visited = False

    for v in G:
        if not v.visited:
            # we must return time, because variable in python are passed by assignment
            time = DFSvisit(v, time)