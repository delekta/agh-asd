# Time complexity O((n-1)!)


def next_vertex(G, X, k, n):
    while True:
        X[k] = ((X[k] + 1) % (n + 1))
        if X[k] == 0:
            return
        if G[X[k - 1]][X[k]] == 1:
            j = 1
            while j < k:
                if X[j] == X[k]:
                    break
                j += 1
            if j == k:
                if k < n or k == n and G[X[k]][X[0]] == 1:
                    return


def cycle(G, X, k, n):
    # if you dont have while true it only prints one result
    while True:
        next_vertex(G, X, k, n)
        if X[k] == 0:
            return
        if k == n:
            print(X)
        # must be else, because if you print you must go to "top" with the same k
        else:
            cycle(G, X, k + 1, n)


graph = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0],
]
graph2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
graph3 = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
]
res = [0 for _ in range(len(graph3) + 1)]
cycle(graph3, res, 1, len(graph3) - 1)
