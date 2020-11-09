# stable decreasing counting sort


class Num:
    def __init__(self, val, typ):
        self.val = val
        self.typ = typ


def print_val_type(arr):
    for ele in arr:
        print(ele.val, ele.typ, " |", end="")


def partition(arr, left, right):
    pivot = arr[right].val
    i = left - 1
    for j in range(left, right):
        if arr[j].val > pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q + 1, right)


def decreasing_counting_sort(arr, r):
    B = [None for _ in range(len(arr))]
    C = [0] * r
    for ele in arr:
        C[ele.val] += 1
    for i in range(r - 1, 0, -1):
        C[i - 1] += C[i]
    for i in range(len(arr) - 1, -1, -1):
        C[arr[i].val] -= 1
        B[C[arr[i].val]] = arr[i]
    for i in range(len(arr)):
        arr[i] = B[i]


el1 = Num(1, "A")
el2 = Num(3, "A")
el3 = Num(5, "A")
el4 = Num(7, "A")

el5 = Num(1, "B")
el6 = Num(3, "B")
el7 = Num(5, "B")
el8 = Num(7, "B")

el9 = Num(1, "C")
el10 = Num(3, "C")
el11 = Num(5, "C")
el12 = Num(7, "C")

el13 = Num(6, "A")
el14 = Num(2, "A")

arr = [el1, el2, el3, el4, el5, el6, el7, el8, el9, el10, el11, el12, el13, el14]
arr2 = arr[:]

print("\nBefore Sort: ", end=" ")
print_val_type(arr)
decreasing_counting_sort(arr, 8)
print("\nCounting Sort: ", end=" ")
print_val_type(arr)

quicksort(arr2, 0, len(arr2) - 1)
print("\nQuick Sort: ", end=" ")
print_val_type(arr2)
