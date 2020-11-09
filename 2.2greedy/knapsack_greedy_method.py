# Fractional Knapsack Problem
# Given weights and values of n items , we need to put these items in a knapsack
# of capacity W to get maximum total value of knapsack in fractional knapsack we
# can break items for maximizing the total value od knapsack


def create_el(item):
    return item[0] / item[1], item[1]


def sort_by_unitary_profit(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i][0] < arr[i + 1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# items is an array of tuples (profit, weight)
def knapsack(items, W):
    unitary_items = []

    # creating array of tuples (unitary profit, weight)
    for i in range(len(items)):
        unitary_items.append(create_el(items[i]))

    # sort in descending order
    sort_by_unitary_profit(unitary_items)
    res = 0
    for item in unitary_items:
        if W - item[1] >= 0:
            res += item[0] * item[1]
            W -= item[1]

        else:
            res += item[0] * W
            break

    return res


arr = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]
W = 6
print(knapsack(arr, W))
