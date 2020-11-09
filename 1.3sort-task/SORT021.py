# Proszę zaimplementować algorytm QuickSort, tak aby
# głębokość stosu rekursji nie przekraczałą O(log(n)).


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    # remember range
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    # remember return
    return i


def quicksort(arr, left, right):
    while left < right:
        pi = partition(arr, left, right)
        if pi - left < right - pi:
            quicksort(arr, left, pi - 1)
            left = pi + 1
        else:
            quicksort(arr, pi + 1, right)
            right = pi - 1


arr = [2, 42, 12, 56, 73, 19, 24, 16, 31]
quicksort(arr, 0, len(arr) - 1)
print(arr)