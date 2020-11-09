# not deep quicksort

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    # remember range
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    # remember return
    return i

def quicksort(arr, low, high):
    while low < high:

        pi = partition(arr, low, high)

        if pi - low < high - pi:

            quicksort(arr, low, pi - 1)
            low = pi + 1

        else:

            quicksort(arr, pi + 1, high)
            high = pi - 1


arr = [2, 4, 54, 23, 6, 76, 5, 46, 48]
quicksort(arr, 0, len(arr) - 1)
print(arr)