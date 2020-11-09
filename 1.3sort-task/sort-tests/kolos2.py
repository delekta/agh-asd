# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy.
# Żołnierze zostaną ustawieni na placu w szeregu malejąco względem wzrostu.
# Proszę zaimplementować funkcję: section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie.
# Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis algorytmu
# oraz proszę oszacować jego złożoność czasową.


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


# Ustawia index na swoje miejsce, zlozonosc czasowa O(n)
def kth_statistic(arr, idx, left, right):
    q = partition(arr, left, right)

    if idx == q:
        return
    elif idx < q:
        kth_statistic(arr, idx, left, q - 1)
    else:
        kth_statistic(arr, idx, q + 1, right)


# Time complexity: O(n)
def height_between_p_q(arr, p, q):
    kth_statistic(arr, q - 1, 0, len(arr) - 1)
    kth_statistic(arr, p - 1, 0, q - 2)  # moge wywolac do q - 2 bo i tak wiemy ze elementy mniejsze od
                                         # q-tego sa za q - 1 i nie ma sensu ich rozwazac
    print(arr)

    res = [None] * (q - p + 1)
    k = 0

    for i in range(p - 1, q):
        res[k] = arr[i]
        k += 1
    return res


arr = [1, 3, 5, 7, 2, 9, 8, 4, 10, 13, 12, 17, 16, 14, 15, 19, 20, 6, 11, 18]

print(arr)
p = 2
q = 10
print("Height between p and q:", height_between_p_q(arr, p, q))
