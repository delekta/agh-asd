# Sortowania liniowe
# Zadanie 1
# Mamy dane n punktow (x, y) w okregu o promieniu k(liczba naturalna), tzn 0 <= x^2 + y^2 <= k ktore sa
# w nim rownomiernie rozlozone, tzn. prawdopodobienstwo znalezenia punktu na danym obszarze jest
# proprcjonalne do pola tego obszaru.
# Napisz algorytm, ktory w czasie O(n) posortuje punkty po odleglosci do punktu (0, 0), tzn
# d = sqrt(x^2 + y^2)
# Wiemy ze prawdopodobienstwo znalezienia punktu na danym obszaze jest proporcjonalne do pola tego obszaru
# wiec musimy podzielic okrag na pierscienie o rownych polach


# d^2
def d_2(el):
    return el[0]*el[0] + el[1]*el[1]


def special_sort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            di = d_2(arr[i])
            dii = d_2(arr[i + 1])
            if dii < di:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# el is a tuple el[0] = x, el[1] = y, (x, y)
def which_bucket(el, k, n):
    # if we divide by "//" k^2, we dont need floor
    # "( k * k)" this bracket is important
    return (d_2(el) * n) // (k * k)


def bucket_sort(arr, k, n):
    buckets = [[] for _ in range(n)]

    for el in arr:
        which = which_bucket(el, k, n)
        buckets[which].append(el)

    res = []
    for bucket in buckets:
        special_sort(bucket)
        res.extend(bucket)

    for i in range(len(arr)):
        arr[i] = res[i]


# k is a radius of circle
k = 7
arr = [(1, 2), (2, 3), (4, 5), (3, 5), (3, 3), (0, 4), (1, 3), (1, 1), (2, 2), (2, 4)]
print(arr)
bucket_sort(arr, k, len(arr))
print(arr)
