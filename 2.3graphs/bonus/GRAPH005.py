# Dany jest graf G = (V,E), gdzie każda krawędź ma wagę ze zbioru {1,...,|E|} (wagi krawędzi są parami różne).
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y,
# w której przechodzimy po krawędziach o coraz mniejszych wagach.


class Vertex:
    def __init__(self, num_of_vertices):
        self.parent = None
        # Because we can visit vertex through different edges
        self.visited_from = [False for _ in range(num_of_vertices)]


def DFS(values, vertices, n, a, b):
    for i in range(n):

        # prevent values[0][0]
        if i != a:

            if values[a][i] != 0:

                if not vertices[i].visited_from[a]:

                    if values[vertices[a].parent][a] > values[a][i]:

                        # We should set properties when it is sure that a is selected
                        vertices[i].parent = a

                        # important because we can reach vertex from other direction, and it can ruin our solution
                        vertices[i].visited_from[a] = True
                        vertices[a].visited_from[i] = True

                        if i == b:
                            return True

                        if DFS(values, vertices, n, i, b):
                            return True
    return False


n = 5
# cost to get from i to j, if value different from 0, edges exist
graph = [
    [0, 3, 5, 10, 0],
    [3, 0, 4, 6, 7],
    [5, 4, 0, 0, 0],
    [10, 6, 0, 0, 0],
    [0, 7, 0, 0, 0],
]

# Needed to check if visited and store parent index
vertices = [Vertex(n) for _ in range(n)]

# preparation arrays to function
vertices[0].parent = 0
graph[0][0] = float('inf')

print(DFS(graph, vertices, n, 0, 4))
