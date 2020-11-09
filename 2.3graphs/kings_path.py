# Tzw. "Algorytm elementarny" wkładamy sztuczne wierzchołki, np jesli krawędz ma wage 3 to wstawiamy 2 dodatkowe
# wierchołki(na tej krawedzi), wtedy wszystkie "sztuczne krawedzie" maja wage 1 i przechodzimy BFS

# Dana jest szachownica o wymiarach n×n. Każde pole (i,j) ma koszt (liczbę ze zbioru{1,...,5}) umieszczony wtablicy
# A (napolu A[j][i]).W lewym górnym rogu szachownicy (napozycji(0,0) stoi król,którego zadaniem jest przejąść do prawego
# dolnego rogu, przechodząc po polach o minimalnym sumarycznym koszcie (jeśli król stoi na polu (i,j) to ponosi
# koszt A[j][i]; tak więc każda trasa zawiera koszt A[0][0] i A[n−1][n−1]). Proszę zaimplementować funkcje kings
# path(A), która oblicza koszt sciezki króla. Funkcja powinna byc mozliwie jak najszybsza (w szczególności oczekujemy
# złożoności O(n2)). Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu
# testującego; sprawdzający może także dołożyć swoje testy):


from queue import PriorityQueue


# działą 02.07.2020
def kings_path(G, src1, src2):
    Q = PriorityQueue()
    dist = [[float('inf') for _ in range(len(G))] for _ in range(len(G))]
    neighbours = [[[] for _ in range(len(G))] for _ in range(len(G))]
    visited = [[False for _ in range(len(G))] for _ in range(len(G))]
    parent = [[-1, -1] for _ in range(len(G))]
    s = [0, (src1, src2), 0]

    for i in range(len(G)):
        for j in range(len(G)):
            if i > 0:                    # ( counter, neighbour_idx,  cost_of_edge)
                neighbours[i][j].append([G[i - 1][j], (i - 1, j), G[i - 1][j]])
            if j > 0:
                neighbours[i][j].append([G[i][j - 1], (i, j - 1), G[i][j - 1]])
            if i < len(G) - 1:
                neighbours[i][j].append([G[i + 1][j], (i + 1, j), G[i + 1][j]])
            if j < len(G) - 1:
                neighbours[i][j].append([G[i][j + 1], (i, j + 1), G[i][j + 1]])

    dist[s[1][0]][s[1][1]] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        if u[0] == 0:
            for neighbour in neighbours[u[1][0]][u[1][1]]:
                if not visited[neighbour[1][0]][neighbour[1][1]]:
                    visited[neighbour[1][0]][neighbour[1][1]] = True
                    dist[neighbour[1][0]][neighbour[1][1]] = dist[u[1][0]][u[1][1]] + neighbour[2]
                    Q.put(neighbour)
        else:
            u[0] -= 1
            Q.put(u)

    print(dist)


A = [
    [1, 1, 4, 5],
    [5, 1, 5, 1],
    [4, 1, 1, 1],
    [4, 1, 3, 3],
]
kings_path(A, 0, 0)
