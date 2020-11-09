
# W jaki sposob zrealizowac strukturę danych, która pozwala wykonywac operacje:
# 1.Insert
# 2.Median heap


def parent(i):
    return i // 2


def move_max_to_min(heap_max, heap_min):
    heap_min.append(heap_max[1])
    heap_max[1], heap_max[heap_max[0] - 1] = heap_max[heap_max[0] - 1], heap_max[1]
    del heap_max[heap_max[0] - 1]
    heap_max[0] -= 1
    heap_min[0] += 1
    heapify_max(heap_max, heap_max[0], 1)

    i = heap_min[0] - 1
    while parent(i) >= 1 and heap_min[i] < heap_min[parent(i)]:
        heap_min[i], heap_min[parent(i)] = heap_min[parent(i)], heap_min[i]
        i = i // 2


def move_min_to_max(heap_max, heap_min):
    heap_max.append(heap_min[1])
    heap_min[1], heap_min[heap_min[0] - 1] = heap_min[heap_min[0] - 1], heap_min[1]
    del heap_min[heap_min[0] - 1]
    heap_min[0] -= 1
    heap_max[0] += 1
    heapify_min(heap_min, heap_min[0], 1)
    # heapify_max(heap_max, heap_max[0], 1)

    i = heap_max[0] - 1
    while parent(i) >= 1 and heap_max[i] > heap_max[parent(i)]:
        heap_max[i], heap_max[parent(i)] = heap_max[parent(i)], heap_max[i]
        i = i // 2


def rebalance(heap_max, heap_min):
    if heap_max[0] - heap_min[0] == 2:
        move_max_to_min(heap_max, heap_min)
    elif heap_min[0] - heap_max[0] == 2:
        move_min_to_max(heap_max, heap_min)


# heap_max[0] -> dlugosc tablicy
def insert_max(heap_max, val):
    heap_max[0] += 1
    i = heap_max[0] - 1
    heap_max.append(val)
    while parent(i) >= 1 and heap_max[i] > heap_max[parent(i)]:
       heap_max[i], heap_max[parent(i)] = heap_max[parent(i)], heap_max[i]
       i = i // 2
    # heapify_max(heap_max, heap_max[0], 1)  #  nie moze być heapify, gdy appendujemy na koniec!!!


def insert_min(heap_min, val):
    heap_min[0] += 1
    i = heap_min[0] - 1
    heap_min.append(val)
    while parent(i) >= 1 and heap_min[i] < heap_min[parent(i)]:
        heap_min[i], heap_min[parent(i)] = heap_min[parent(i)], heap_min[i]
        i = i // 2
    # heapify_min(heap_min, heap_min[0], 1)  #  nie moze być heapify, gdy appendujemy na koniec!!!


def insert(heap_max, heap_min, val):
    if heap_max[0] == 1:
        heap_max.append(val)
        heap_max[0] += 1
    elif val < heap_max[1]:
        insert_max(heap_max, val)
    else:
        insert_min(heap_min, val)

    rebalance(heap_max, heap_min)


def get_median(heap_max, heap_min):
    if heap_max[0] == heap_min[0]:
        return float((heap_max[1] + heap_min[1]) / 2)
    elif heap_max[0] - heap_min[0] == 1:
        return heap_max[1]
    else:
        return heap_min[1]


def heapify_min(arr, length, root):
    left = 2 * root
    right = 2 * root + 1
    mini = root
    if left < length and arr[left] < arr[mini]:
        mini = left
    if right < length and arr[right] < arr[mini]:
        mini = right
    if mini != root:
        arr[root], arr[mini] = arr[mini], arr[root]
        heapify_min(arr, length, mini)


def heapify_max(arr, length, root):

    left = 2 * root
    right = 2 * root + 1
    biggest = root

    if left < length and arr[left] > arr[biggest]:
        biggest = left
    if right < length and arr[right] > arr[biggest]:
        biggest = right
    if biggest != root:
        arr[biggest], arr[root] = arr[root], arr[biggest]
        heapify_max(arr, length, biggest)


def build_heap_max(arr):
    # build heap to 0, because 0 is length of array
    for i in range((arr[0] - 1) // 2, 0, -1):
        heapify_max(arr, arr[0], i)


def build_heap_min(arr):
    # build heap to 0, because 0 is length of array
    for i in range((arr[0] - 1) // 2, 0, -1):
        heapify_min(arr, arr[0], i)


def print_heap(heap):
    enter = 1
    for i in range(1, heap[0]):
        print(heap[i], end=" ")
        if i == enter:
            print()
            enter = i * 2 + 1


# heap[0] == 1 -> heap is empty
heap_max = [1]
heap_min = [1]
insert(heap_max, heap_min, 8)
insert(heap_max, heap_min, 74)
insert(heap_max, heap_min, 18)
insert(heap_max, heap_min, 13)
insert(heap_max, heap_min, 12)
insert(heap_max, heap_min, 9)
insert(heap_max, heap_min, 3)
insert(heap_max, heap_min, 35)
insert(heap_max, heap_min, 16)
insert(heap_max, heap_min, 50)
insert(heap_max, heap_min, 10)
insert(heap_max, heap_min, 45)
insert(heap_max, heap_min, 5)
insert(heap_max, heap_min, 8)
insert(heap_max, heap_min, 14)
insert(heap_max, heap_min, 47)
# build_heap_max(heap_max)
# build_heap_min(heap_min)
print_heap(heap_max)
print("\n")
print_heap(heap_min)
print("\nMediana:",get_median(heap_max, heap_min))
