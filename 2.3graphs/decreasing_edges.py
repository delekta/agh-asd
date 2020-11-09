# Dany jest graf G = (V,E), gdzie każda krawędź ma wagę ze zbioru {1,...,|E|} (wagi krawędzi są parami różne).
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y,
# w której przechodzimy po krawędziach o coraz mniejszych wagach.


class vertex:
    def __init__(self, idx):
        self.idx = idx
        self.lastMax = 0


#we have a graph G = (V,E) given as adjacency list and wages of our egdes, x - start, y - end
def DFS_exist_increasing_paths(G, W, x, y):

    def DFSVisit(x,y):
        if x == y:
            return True
        for neighbour in G[x]:
            if W[x][neighbour] > V[neighbour].lastMax and W[x][neighbour] < V[x].lastMax:
                V[neighbour].lastMax = W[x][neighbour]
                if DFSVisit(neighbour, y):
                    return True
            else:
                continue
        return False

    n = len(G)
    V = [vertex(i) for i in range(n)]
    V[x].lastMax = float('inf')
    return DFSVisit(x,y)