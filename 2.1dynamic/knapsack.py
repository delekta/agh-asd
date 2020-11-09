# Zadanie 1
# Proszę zaimplementować rozwiązanie problemu plecakowego przy pomocy rekurencji ze spamiętywaniem.

# W -> Weight
# P -> Profit
# MaxW -> Max Profit
def Knapsack(W, P, MaxW):
    n = len(W)
    F = [None] * n
    for i in range(n):
        F[i] = [0] * (MaxW + 1)
    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i - 1][w], F[i - 1][w - W[i]] + P[i])

    return F[n - 1][MaxW]


W = [4, 1, 2, 4, 3, 5, 10, 3]
P = [7, 3, 2, 10, 4, 1, 7, 2]

print(Knapsack(W, P, 10))




