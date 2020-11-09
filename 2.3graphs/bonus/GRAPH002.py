# (uniwersalne ujście) Mówimy, że wierzchołek t w graﬁe skierowanym jest uniwersalnym ujściem, jeśli
# (a) z każdego innego wierzchołka v istnieje krawędź z v do t
# (b) nie istnieje żadna krawędź wychodząca z t.
# Proszę podać algorytm znajdujący ujście (jeśli istnieje) przy reprezentacji macierzowej grafu.


def ujscie(G, n):
    i = 0
    j = 0
    while i < n and j < n:
        if G[i][j] == 0:
            j += 1
        elif G[i][j] == 1:
            i += 1
    if i == n:
        return False
    elif j == n:
        for k in range(n):
            if G[i][k] != 0:
                return False
            if G[k][i] != 1:
                if k != i:
                    return False
    return True


# adjacency matrix
good = [
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],  # t = 4
    [0, 0, 0, 0, 1, 0],
]

bad = [
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]

n = 6
print(ujscie(good, n))
print(ujscie(bad, n))




