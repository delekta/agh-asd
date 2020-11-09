# Zaimplementuj funkcję average_score(arr, n, lowest, highest).
# Funkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych
# (ich rozkład nie jest znany, ale wszystkie są parami różne) i zwraca
# średnią wartość podanych liczb po odrzuceniu lowest najmniejszych
# oraz highest największych. Zaimplementowana funkcja powinna być
# możliwie jak najszybsza. Oszacuj jej złożoność czasową (oraz bardzo
# krótko uzasadnić to oszacowanie).
import random
import time


def random_partition(arr, left, right):
    rdm = random.randrange(left, right + 1)
    arr[rdm], arr[right] = arr[right], arr[rdm]
    return partition(arr, left, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[right], arr[i] = arr[i], arr[right]
    return i


def kthstatistic(arr, left, right, k):
    if left == right:
        return arr[left]

    pi = random_partition(arr, left, right)
    print(arr, pi)
    size = pi - left + 1

    if size == k:
        # wazne returnujesz arr[pi]!!!
        return arr[pi]

    elif k < size:
        return kthstatistic(arr, left, pi - 1, k)
    else:
        return kthstatistic(arr, pi + 1, right, k - size)


def arithmetic_average(arr, lowest, highest):
    # np 3 najwiekszy przy dziesiecio elementowej tablicy bedzie mial indeks 7
    high = len(arr) - highest + 1
    kthstatistic(arr, 0, len(arr) - 1, lowest)
    kthstatistic(arr, 0, len(arr) - 1, high)
    print(lowest, high)

    sum = 0
    # dobry range, bo lowest i high to nie indeksy
    for i in range(lowest, high - 1):
        sum += arr[i]
    print(sum, high - lowest - 1)
    return sum / (high - lowest - 1)

random.seed(time.time())
arr = [5, 7, 9, 8, 6, 4, 1, 3, 2, 10, 20, 18, 14, 16, 13, 16, 11, 12, 17, 19, 15]
arr2 = [10, 30, 20, 40]
res = arithmetic_average(arr, 5, 5)
print(res)





