#Cormen "Introduction to algorithms"

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q + 1, right)

arr = [2, 6, 17, 23, 45, 1, 45, 27, 19, 14, 5]

print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)