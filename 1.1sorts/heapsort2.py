def parent(i):
    return i // 2


def left_kid(i):
    return 2 * i


def right_kid(i):
    return 2 * i + 1


def build_heap(arr):
    # build heap to 0 beacuse 0 is length of array
    for i in range(arr[0] // 2, 0, -1):
        heapify(arr, i)


def heapify(arr, root):
    l = left_kid(root)
    r = right_kid(root)
    maks = root
    if l < arr[0] and arr[l] > arr[maks]:
        maks = l
    if r < arr[0] and arr[r] > arr[maks]:
        maks = r
    if maks != root:
        arr[maks], arr[root] = arr[root], arr[maks]
        heapify(arr, maks)


# arr[0] -> length of table
def heapsort(arr):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        # remember 0 is length of array
        arr[1], arr[i] = arr[i], arr[1]
        arr[0] -= 1
        heapify(arr, 1)


arr = [1, 5, 13, 2, 34, 23, 12, 7, 8, 13, 56]
arr[0] = len(arr)
print(arr)
heapsort(arr)
print(arr)