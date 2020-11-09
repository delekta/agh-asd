# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać na prom. Prom ma dwa pasy
# (lewy i prawy), oba długości D. Proszę napisać program, który wyznacza, które samochody powinny pojechać na który
# pas, żeby na promie zmieściło się jak najwięcej aut. Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane
# w tablicy A.
# It's quite easy to do in O(2^cars) with backtracking - we load car on the left and try all the possibilities then,

# Optimal solution:
# Let us call s, the sum of the length of the cars in the solution from the knapsack problem. If the sum of all the
# cars length - s is less or equal than d, then all the cars considered for solving the knapsack problems can fit in
# the ferry (one lane being all those selected to be part of the knapsack solution, the other lane being the rest).
# If the sum of the length of the rest of the cars is more than d, then all the cars cannot fit in the ferry.
# Remove the last car from the list of the cars, and solve again the knapsack problem. Do this until the sum
# of the length of the not selected cars is below d.

# we save maximum and load car on the right and do the same saving max again.
# The complexity of the DP algorithm to solve the knapsack problem is O(nd)
# and it needs to be solved at most n times -> complexity O(n^2d)

def knapsack_0_1(cars, n, len_lane):
    f = [[0 for _ in range(len_lane + 1)] for _ in range(n)]

    for i in range(cars[0], len_lane + 1):
        f[0][i] = cars[0]

    for i in range(1, n):
        for j in range(1, len_lane + 1):
            f[i][j] = f[i - 1][j]
            if j > cars[i]:
                f[i][j] = max(f[i][j], f[i - 1][j - cars[i]] + cars[i])
    return f[n - 1][len_lane]


def loading_ferry(cars, len_lane):
    res = -1
    for n in range(len(cars), 0, -1):
        total_length = 0
        for i in range(n):
            total_length += cars[i]

        taken = knapsack_0_1(cars, n, len_lane)
        rest = total_length - taken
        # print(rest)
        if rest <= len_lane:
            res = n
            break
    return res


cars = [5, 7, 5, 3, 3, 3, 2]
d = 10
print(loading_ferry(cars, d))