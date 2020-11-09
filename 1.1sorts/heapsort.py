
# for heap min
def heapify_min(arr, length, root):
    left = 2 * root + 1
    right = 2 * root + 2
    mini = root
    if left < length and arr[left] < arr[mini]:
        mini = left
    if right < length and arr[right] < arr[mini]:
        mini = right
    if mini != root:
        arr[root], arr[mini] = arr[mini], arr[root]
        heapify_min(arr, length, mini)


# for heap max
def heapify_max(arr, length, root):

    left = 2 * root + 1
    right = 2 * root + 2
    biggest = root

    if left < length and arr[left] > arr[biggest]:
        biggest = left
    if right < length and arr[right] > arr[biggest]:
        biggest = right
    if biggest != root:
        arr[biggest], arr[root] = arr[root], arr[biggest]
        heapify_max(arr, length, biggest)


def heap_sort(arr):
    length = len(arr)
    for i in range(length - 1, -1, -1):
        # prepering max heap
        heapify_max(arr, length, i)
    for j in range(length - 1, 0, -1):
        arr[j], arr[0], = arr[0], arr[j]
        # "j" will be also a size of the heap that we still need to heapify
        heapify_max(arr, j, 0)


arr = [2, 2, 3, 1, 5, 0, 12, 13, -3, 159, 23, 2, 3, 13, 24, 13]
print(arr)
heap_sort(arr)
print(arr)


