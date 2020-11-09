# Dwuwymiarowy Problem Plecakowy
# Proszę zaimplementować funkcję knapsack2d(P, max w, max h), która oblicza maksymalną
# wartość plecaka w dwuwymiarowej wersji dyskretnego problemu plecakowego, określonego
# następująco. Mamy daną tablicę n trójek P = [(v0,w0,h0),...(vn−1,wn−1,hn−1)],
# gdzie i-ta krotka ma następujące znaczenie: vi to wartość i-go przemiotu, wi to jego
# waga, a hi to jego wysokość. Złodziej chce wybrać przedmioty o maksymalnej symarycznej
# wartości, których łączna waga nie przekracza danej liczby max w oraz których łączna
# wysokość nie przekracza danej liczby max h (przedmioty zapakowane są w kartony, które
# złodziej układa jeden na drugim).
# def knapsack2d( V, max_w, max_h ):
#
# P = [(5,10,3), (7,8,12), (2,7,3)]
# print( knapsack2d( P, 16, 15 ) # wypisze 9


# debugging needed 25.04.2020
def knapsack2D(items, max_weight, max_height):
    # initialization
    f = [[[0 for _ in range(max_height + 1)] for _ in range(max_weight + 1)] for _ in range(len(items))]

    for w in range(items[0][1], max_weight + 1):
        for h in range(items[0][2], max_height + 1):
            f[0][w][h] = items[0][0]

    for i in range(1, len(items)):
        for w in range(1, max_weight + 1):
            for h in range(1, max_height + 1):
                f[i][w][h] = f[i - 1][w][h]
                if w - items[i][1] >= 0 and h - items[i][2] >= 0:
                    f[i][w][h] = max(f[i - 1][w][h], f[i - 1][w - items[i][1]][h - items[i][2]] + items[i][0])

    res = f[len(items) - 1][max_weight][max_height]
    print_which_items(f, items, max_weight, max_height)
    return res


def print_which_items(f, items, max_weight, max_height):
    res = []
    w = max_weight
    h = max_height
    for i in range(len(items) - 1, 0, -1):
        if f[i][w][h] == 0:
            break
        if f[i][w][h] == f[i - 1][w][h]:
            if i == 1 and f[i - 1][w][h] != 0:
                res.append(0)
            continue

        else:
            res.append(i)
            w -= items[i][1]
            h -= items[i][2]
        if w <= 0 or h <= 0:
            break
    print(res)


P = [(5, 10, 3), (7, 8, 12), (2, 6, 3), (6, 4, 14), (9, 6, 12), (4, 4, 4), (8, 4, 7), (1, 1, 1)]
max_weight = 16
max_height = 15
print(knapsack2D(P, max_weight, max_height))

