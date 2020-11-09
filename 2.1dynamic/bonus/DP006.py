# Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach
# wyrażoną zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n
# metrów. Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.
# ● Dla pręta długości n mamy 2^n-1 możliwości - eksponencjalna wielkość, brute force nie zadziała
# ● Szukamy optymalnego rozwiązania problemu


# my function, more operations than max_cut2
def max_cut(price, n):
    res = [0] * (n + 1)

    # ciecia dlugosci i
    for i in range(1, n):
        print(res)
        for j in range(1, n - i + 1):
            if res[j] + price[i] > res[j + i]:
                res[j + i] = res[j] + price[i]

    return res[n]


def max_cut2(price, n):
    res = [0] * n

    for i in range(1, n):
        for j in range(1, i + 1):
            if res[i - j] + price[j] > res[i]:
                res[i] = res[i - j] + price[j]

    return res[n - 1]


# price[i] -> price of bar length = i
# must be 0 value at index 0 because we want to e.g 5 represent price of length 2(i)
#           1| 2| 3| 4|  5|  6|  7|  8|  9|  10|
price = [0, 1, 5, 9, 10, 10, 17, 17, 20, 24, 25]
print(max_cut(price, len(price)))
