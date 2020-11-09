# Merge M sorted lists of variable length, print them in sorted order efficiently
# Min - heap

# we can do the same with tuples
class Element:
    def __init__(self, data, i):
        self.val = data
        self.idx = i


def swap_elements(el1, el2):
    el1.val, el2.val = el2.val, el1.val
    el1.idx, el2.idx = el2.idx, el1.idx

def heapify_min(arr, length, root):
    left = 2 * root + 1
    right = 2 * root + 2
    mini = root
    if left < length and arr[left].val < arr[mini].val:
        mini = left
    if right < length and arr[right].val < arr[mini].val:
        mini = right
    if mini != root:
        # to cos zmienilo arr[root].val
        swap_elements(arr[root], arr[mini])
        heapify_min(arr, length, mini)


def build_heap(arr):
    # build heap to 0, because 0 is length of array
    for i in range(((len(arr)) // 2) - 1, -1, -1):
        heapify_min(arr, len(arr), i)


def push(heap, el, i):
    ele = Element(el, i)
    heap[0] = ele
    heapify_min(heap, len(heap), 0)


def pop(heap):
    return heap[0]


def heap_empty(heap):
    if len(heap) == 0:
        return True
    else:
        return False


def print_heap(heap):
    for i in range(len(heap)):
        print(heap[i].val, end=" ")


def merge(arr_all):
    merged = []
    heap = [0] * len(arr_all)
    indices = [0] * len(arr_all)
    for i in range(len(arr_all)):
        ele = Element(arr_all[i][0], i)
        heap[i] = ele

    build_heap(heap)

    while not heap_empty(heap):
        popped = pop(heap)
        merged.append(popped.val)
        i = popped.idx
        indices[i] += 1
        if indices[i] == len(arr_all[i]):
            heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
            del heap[len(heap) - 1]
            heapify_min(heap, len(heap), 0)
        else:
            push(heap, arr_all[i][indices[i]], i)

    print(merged)


"""
TUPLES INSTEAD OF CLASS "Elements"
"""


def build_heapT(arr):
    # build heap to 0, because 0 is length of array
    for i in range(((len(arr)) // 2) - 1, -1, -1):
        heapify_minT(arr, len(arr), i)


def mergeT(arr_all):
    merged = []
    heap = [0] * len(arr_all)
    indices = [0] * len(arr_all)
    for i in range(len(arr_all)):
        ele = (arr_all[i][0], i)
        heap[i] = ele

    build_heapT(heap)

    while not heap_empty(heap):
        popped = pop(heap)
        merged.append(popped[0])
        i = popped[1]
        indices[i] += 1
        if indices[i] == len(arr_all[i]):
            heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
            del heap[len(heap) - 1]
            heapify_minT(heap, len(heap), 0)
        else:
            pushT(heap, arr_all[i][indices[i]], i)

    print(merged)

def pushT(heap, el, i):
    ele = (el, i)
    heap[0] = ele
    heapify_minT(heap, len(heap), 0)


def heapify_minT(arr, length, root):
    left = 2 * root + 1
    right = 2 * root + 2
    mini = root
    if left < length and arr[left][0] < arr[mini][0]:
        mini = left
    if right < length and arr[right][0] < arr[mini][0]:
        mini = right
    if mini != root:
        # to cos zmienilo arr[root].val
        arr[mini], arr[root] = arr[root], arr[mini]
        heapify_minT(arr, length, mini)



arr1 = [10, 20, 30, 40, 69]
arr2 = [15, 25, 35, 37]
arr3 = [27, 29, 37, 48, 93]
arr4 = [32, 33]
arr_all = [arr4, arr3, arr1, arr2]

mergeT(arr_all)


