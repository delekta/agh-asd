# heapify max wymaga dopracowania

def on_level(arr, idx):
    i = 1
    res = 0
    if idx == 0:
        return res
    while i < len(arr):
        if pow(2, i) - 1 <= idx < pow(2, i + 1) - 2:
            res = i
            break
        i += 1
    return res


def peekmin(array):
    return array[0]


def peekmax(array, size):
    if size == 1:
        return array[0]
    elif size == 2:
        return array[1]
    else:
        return max(array[1], array[2])


def heapify_min(arr, size, root):
    if size > root * 2 + 1:  # i has children
        mini = root * 2 + 1
        if root * 2 + 2 < size and arr[root * 2 + 2] < arr[mini]:
            mini = root * 2 + 2
        child = True
        for j in range(root * 4 + 3, min(root * 4 + 7, size)):
            if arr[j] < arr[mini]:
                mini = j
                child = False

        if child:
            if arr[mini] < arr[root]:
                arr[root], arr[mini] = arr[mini], arr[root]
        else:
            if arr[mini] < arr[root]:
                if arr[mini] < arr[root]:
                    arr[mini], arr[root] = arr[root], arr[mini]
                if arr[mini] > arr[(mini - 1) // 2]:
                    arr[mini], arr[(mini - 1) // 2] = arr[(mini - 1) // 2], arr[mini]
                heapify_min(arr, size, mini)


def heapify_max(arr, size, root):
    if size > root * 2 + 1:  # i has children
        maks = root * 2 + 1
        if root * 2 + 2 < size and arr[root * 2 + 2] > arr[maks]:
            maks = root * 2 + 2
        child = True
        for j in range(root * 4 + 3, min(root * 4 + 7, size)):
            if arr[j] > arr[maks]:
                maks = j
                child = False

        if child:
            if arr[maks] > arr[root]:
                arr[root], arr[maks] = arr[maks], arr[root]
        else:
            if arr[maks] > arr[root]:
                if arr[maks] > arr[root]:
                    arr[maks], arr[root] = arr[root], arr[maks]
                if arr[maks] < arr[(maks - 1) // 2]:
                    arr[maks], arr[(maks - 1) // 2] = arr[(maks - 1) // 2], arr[maks]
                heapify_max(arr, size, maks)


def minmaxheapproperty(array, size):
    for i, k in enumerate(array[:size]):
        if on_level(i) % 2 == 0:  # min level
            # check children to be larger
            for j in range(2 * i + 1, min(2 * i + 3, size)):
                if array[j] < k:
                    print(array, j, i, array[j], array[i], on_level(i))
                    return False
            # check grand children to be larger
            for j in range(4 * i + 3, min(4 * i + 7, size)):
                if array[j] < k:
                    print(array, j, i, array[j], array[i], on_level(i))
                    return False
        else:
            # check children to be smaller
            for j in range(2 * i + 1, min(2 * i + 3, size)):
                if array[j] > k:
                    print(array, j, i, array[j], array[i], on_level(i))
                    return False
            # check grand children to be smaller
            for j in range(4 * i + 3, min(4 * i + 7, size)):
                if array[j] > k:
                    print(array, j, i, array[j], array[i], on_level(i))
                    return False

    return True


def heapify(arr, size,root):
    level = on_level(arr, root)
    if level % 2 == 0:
        heapify_min(arr, size, root)
    else:
        heapify_max(arr, size, root)


def build_heap(arr, size):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, size, i)


def heapsort(arr):
    size = len(arr)
    build_heap(arr, size)
    min = peekmin(arr)
    max = peekmax(arr, size)
    print("max:", max)
    print("min", min)


arr = [1, 6, 8, 13, 52, -2, -55, -7, -18, 5, 4, 10, 62, -13]

heapsort(arr)
