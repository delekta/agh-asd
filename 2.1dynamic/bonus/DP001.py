# Knapsack problem 0/1


def knapsack(profit, weight, max_weight):
    # 2D list comprehansive
    F = [[0 for _ in range(max_weight + 1)] for _ in range(len(profit))]
    for i in range(max_weight + 1):
        if i >= weight[0]:
            F[0][i] = profit[0]
    for i in range(len(profit)):
        F[i][0] = 0
    for y in range(1, len(profit)):
        for x in range(1, max_weight + 1):
            F[y][x] = F[y - 1][x]
            if x - weight[y] >= 0:
                F[y][x] = max(F[y - 1][x], F[y - 1][x - weight[y]] + profit[y])

    res = F[len(profit) - 1][max_weight]
    w = max_weight
    items = []
    for i in range(len(profit) - 1, -1, -1):

        # exception
        # you can prevent from by making F[0][i] all = 0
        if i == 0:
            if res != 0:
                items.append(0)
            else:
                continue

        elif res == F[i - 1][w]:
            continue

        else:
            items.append(i)
            res -= profit[i]
            w -= weight[i]

    return items


profit = [1, 3, 4, 7, 3, 9]
weight = [3, 5, 3, 8, 2, 8]
max_weight = 8
print(knapsack(profit, weight, max_weight))
