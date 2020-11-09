# Zadanie 2
# Proszę zaimplementować rozwiązanie problemu plecakowego tak, żeby funkcjazwracały listę indeksów przedmiotów,
# które należy wybrać (można korzystać zfunkcjiappenddo dopisywania elementów na końcu listy).


# W -> Weight
# P -> Profit
# WHICH -> which element we take
# MaxW -> Max WEIGHT
def Knapsack(W, P, MaxW, WHICH):
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

    res = F[n - 1][MaxW]

    # print max value we can take
    print(res)

    # w -> curr_weight
    w = MaxW
    for i in range(n, 0, -1):
        if res <= 0:
            break

        # jesli nasza aktualna wartosc jest rowna wartosci dla elementu o
        # jeden mniejszego to znaczy ze nie wzielismy tego elementu
        if res == F[i - 1][w]:
            # edge case, if we take element 0
            if i - 1 == 0 and res != 0:
                WHICH.append(0)
            else:
                continue

        else:
            WHICH.append(i)
            res -= P[i]
            w -= W[i]

    print(WHICH)


W = [1, 2, 3, 4, 5, 4, 10, 3]
P = [3, 2, 4, 10, 1, 7, 7, 2]
MaxW = 10
WHICH = []

Knapsack(W, P, MaxW, WHICH)

