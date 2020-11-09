# kth-statistic
# kth smallest/largest element in unsorted array (expected linear time)
# using quicksort based method
# Czy da sie lepiej? 14.03.2020
import random
import time


def random_partition(arr, left, right):
    n = random.randrange(left, right + 1)
    arr[right], arr[n] = arr[n], arr[right]
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


def kth_smallest(arr, left, right, k):
    q = random_partition(arr, left, right)
    print(q, arr)
    if q == k - 1:
        return arr[q]
    if k - 1 < q:
        # you must return cause all function is "return function"
        return kth_smallest(arr, left, q - 1, k)
    elif k - 1 > q:
        return kth_smallest(arr, q + 1, right, k)


if __name__ == "__main__":
    random.seed(time.time())
    arr = [12, 2, 64, 34, 32, 87, 4, 93, 13, 42, 18]
    print(kth_smallest(arr, 0, len(arr) - 1, 9))
