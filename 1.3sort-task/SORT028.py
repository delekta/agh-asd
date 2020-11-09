# Zadanie 7
# Dana jest tablica zawierająca n liczb z zakresu [0...n^2-1]. Napisz algorytm, który posortuje taką
# tablicę w czasie O(n).
# Pomysl: Zwykły Counting Sort najpierw po modulach n a pozniej po dzieleniu calkowitoliczbowym przez n

def counting_sort_modul(A, n):
    B = [0] * len(A)
    C = [0] * n
    for i in range(len(A)):
        C[A[i] % n] += 1
    for j in range(1, n):
        C[j] += C[j - 1]
        # we must take elements from the end to make counting sort stable
    for k in range(len(A) - 1, -1, -1):
        C[A[k] % n] -= 1    # sum of prefix elements
        B[C[A[k] % n]] = A[k]
    return B

def counting_sort_int_div(A, n):
    B = [0] * len(A)
    C = [0] * n
    for i in range(len(A)):
        C[A[i] // n] += 1
    for j in range(1, n):
        C[j] += C[j - 1]
        # we must take elements from the end to make counting sort stable
    for k in range(len(A) - 1, -1, -1):
        C[A[k] // n] -= 1    # sum of prefix elements
        B[C[A[k] // n]] = A[k]
    return B

def sort(arr):
    n = len(arr)
    res = counting_sort_modul(arr, n)
    res = counting_sort_int_div(arr, n)
    return res


arr = [5, 1, 16, 9, 24]
print(arr)
new = sort(arr)
print(new)
