#  Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji
#  ma mapę zatoki w postaci tablicy M, gdzie M[y][x] to głebokość zatoki na pozycji (x,y). Jeśli jest ona
#  większa niż pewna wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0,0)
#  a port znajduje się na pozycji (n−1,m−1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na
#  pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden).
#  Proszę napisać funkcję rozwiązującą problem kapitana.


class Vertex:
    def __init__(self, indices):
        self.visited = False
        self.indices = indices


# Works perfectly 11.04.2020
def creating_array_of_neighbours(M, T, n):
    vertices = [[Vertex((i, j)) for j in range(n)] for i in range(n)]
    vertices[0][0].visited = True
    neighbours = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + 1 < n and M[i + 1][j] > T:
                neighbours[i][j].append(vertices[i + 1][j])
            if j + 1 < n and M[i][j + 1] > T:
                neighbours[i][j].append(vertices[i][j + 1])
            # really important >"=" 0 !!!
            if i - 1 >= 0 and M[i - 1][j] > T:
                neighbours[i][j].append(vertices[i - 1][j])
            if j - 1 >= 0 and M[i][j - 1] > T:
                neighbours[i][j].append(vertices[i][j - 1])

    return neighbours


def DFS(neighbours, n, i=0, j=0):
    for u in neighbours[i][j]:
        if u.indices == (n - 1, n - 1):
            return True
        if not u.visited:
            u.visited = True
            y, x = u.indices
            if DFS(neighbours, n, y, x):
                return True
    return False


# Not working for every input, only if we can move right and down
def is_possible(M, T, n, i=0, j=0):
    if i == n - 1 and j == n - 1:
        return True
    if i >= n:
        return False
    elif j >= n:
        return False
    else:
        if i + 1 < n and M[i + 1][j] > T:
            # really important if, returns only when is_possible is True
            if is_possible(M, T, n, i + 1, j):
                return True
        if j + 1 < n and M[i][j + 1] > T:
            if is_possible(M, T, n, i, j + 1):
                return True
        # important returns False, when there is no path, without it returns None
        return False


arr = [
    [6, 6, 6, 1, 1],
    [1, 1, 6, 1, 1],
    [6, 6, 6, 1, 1],
    [6, 1, 1, 1, 1],
    [6, 6, 6, 1, 6],
]

T = 5
n = 5
print(is_possible(arr, T, n))

neighbours = creating_array_of_neighbours(arr, T, n)

# checking neighbours
for i in range(n):
    for j in range(n):
        if neighbours[i][j]:
            print(i, j, end=" ")
            for k in range(len(neighbours[i][j])):
                print(neighbours[i][j][k].indices, end=" ")
        print("\n")

print(DFS(neighbours, n))


