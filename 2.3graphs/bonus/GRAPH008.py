# Dany jest spójny graf, potencjalnie bardzo gęsty. Podaj algorytm, który w czasie O(V), sprawdzi, czy
# graf zawiera cykl.
# Pomysł: Najwazniejsza informacja to to ze graf jest spojny, jesli graf jest spojny i acykliczny to jest drzewem
# Jezeli jest drzewem to ma n - 1 krawedzi, mniej krawedzi nie moze miec bo jest spojny, jezeli ma wiecej krawedzi
# to nie jest drzewem, a jest spojny, czyli ma cykl
# Jezeli w DFS odwiedzimy wiecej niz n - 1 krawedzi, gdzie n to liczba wierzcholkow to graf ma cykl


class Vertex:
    def __init__(self, idx):
        self.parent = None
        self.visited = False
        self.idx = idx


# count edges, if edges >= n, graph has cycle
def DFS(v, neighbours, c=0):
    v.visited = True
    for u in neighbours[v.idx]:
        if not u.visited:
            u.parent = v
            # print("normal", v.idx, u.idx)
            c += 1
            c = DFS(u, neighbours, c)
        elif u.visited and v.parent != u:
            # repair in this particular case
            u.parent = v
            # print("not normal", v.idx, u.idx)
            c += 1
        # if c >= len(neighbours):
        #     break
    return c


n = 5
vertices = [Vertex(i) for i in range(n)]
neighbours = [[vertices[1], vertices[2]], [vertices[0], vertices[2]], [vertices[0], vertices[1], vertices[3],
            vertices[4]], [vertices[2]], [vertices[2]]]

print(DFS(vertices[0], neighbours))
