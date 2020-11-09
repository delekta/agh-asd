# Zastosowanie reprezentacji macierzowej grafu
# Mając dany graf w postaci macierzy, sprawdź, czy
# istnieje w nim cykl o długości k.

# Rozwiązanie: Podnosząc macierz adjacencji do potęgi k, otrzymuję w indeksie [i][j] liczbę marszrut o długości k, z
# wierzchołka i do j. Należy zatem podnieść macierz adjacencji do potęgi k, i sprawdzić czy gdzieś w
# [i][i] mamy 1. Złożoność O(V^3*log(k)). W praktyce można osiągnąć złożoność O(V^2.7 * log(k)). W
# teorii… O(V^2.3 * log(k)).
# Marszruta w grafie to skończony ciag krawedzi, odpowiada to tylko grafowi skierowanemu, w grafie nieskierowanym
# Krawedzi 1-4, 4-1 liczona jest jako cykl długosci 2


def multiplying_matrix(M1, M2, length):
    RES = [[0 for _ in range(length)] for _ in range(length)]
    res = 0
    for row in range(length):
        for column in range(length):
            for idx in range(length):
                res += M1[row][idx] * M2[idx][column]
            RES[row][column] = res
            res = 0  # important to reset res

    return RES


def print_matrix(M, length):
    for i in range(length):
        for j in range(length):
            print(M[i][j], end=" ")
        print("\n")

M = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
]

M2 = [
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

n = 5
POW2 = multiplying_matrix(M2, M2, n)
POW3 = multiplying_matrix(POW2, M2, n)
POW4 = multiplying_matrix(POW2, POW2, n)  # we can also multiply POW3 and M

print_matrix(POW2, n)


