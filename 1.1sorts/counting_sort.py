# counting sort cormen verion

# r - range of values in arr [0, r)
def counting_sort(A, r):
    B = [0] * len(A)
    C = [0] * r
    for i in range(len(A)):
        C[A[i]] += 1
    for j in range(1, len(C)):
        C[j] += C[j - 1]
        # we must take elements from the end to make counting sort stable
    for k in range(len(A) - 1, -1, -1):
        C[A[k]] -= 1    # sum of prefix elements
        B[C[A[k]]] = A[k]
    return B


# range [min_v, min_v + r_size)
def counting_sort_range(A, r_size, min_v):
    B = [0] * len(A)
    C = [0] * r_size
    for i in range(len(A)):
        # - min_V jesli min_v > 0, jesli nie to +min_v
        C[A[i] - min_v] += 1
    for j in range(1, len(C)):
        C[j] += C[j - 1]
    for k in range(len(A) - 1, -1, -1):
        C[A[k] - min_v] -= 1
        B[C[A[k] - min_v]] = A[k]
    return B


arr = [1, 3, 3, 2, 1, 1, 4, 2, 2, 1, 3, 5, 2]
print(arr)
arr = counting_sort(arr, 6)
print(arr)
arr2 = [11, 13, 13, 12, 11, 11, 14, 12, 12, 11, 13, 15, 12]
print(arr2)
arr2 = counting_sort_range(arr2, 6, 10)
print(arr2)

# Note:
arr7 = [0] * 3
# W niektorych przypadkach lepsze
# Np jak robisz liste list list = [ [] for _ in range(len) ]
arr8 = [0 for _ in range(3)]
print("arr7:", arr7)
print("arr8:", arr8)
arr_max = [13, 14, 22, 1, 9, 17]
print(max(arr_max)) # funkcja dajaca element maksymalny z tablicy

# Dwa sposoby przepisania literek ze stringa do odzielnych szufladek tablicy
# First
list1 = []
for letter in 'jakub':
    list1.append(letter)
print(list1)

# Second
list2 = [letter for letter in 'kamil']
print(list2)

