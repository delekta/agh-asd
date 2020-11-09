# Sortowania liniowe
# Zadanie 5
# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej
# tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który
# posortuje tablicę w czasie O(n).
# Pomysl: nie ma mowy nic o zlozonosci pamieciowej, wiec mozemy tworzyc dodatkowe tablice
# Przepisujemy ten 10 elementow do nowej tablicy, sortujemy ja, zakladamy ze sortowanie 10 elementowej tablicy
# odbywa sie w czasie stalym, pozostala tablice sortujemy Counting Sortem i na koniec scalamy dwie tablice
# przechodzac raz i wpisujac do wynikowej talbicy zawsze element mniejszy


def counting_sort(A, r):
    B = [0] * (len(A))
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


def _sort(arr, k):
    ten = []
    other = []
    for i in range(len(arr)):
        if arr[i] < 0 or arr[i] > k:
            ten.append(arr[i])
        else:
            other.append(arr[i])

    ten.sort()

    # because [0, k]
    other = counting_sort(other, k + 1)

    res = [0] * len(arr)
    i, j, r = 0, 0, 0
    while i < len(other) and j < len(ten):
        if other[i] < ten[j]:
            res[r] = other[i]
            i += 1
            r += 1
        else:
            res[r] = ten[j]
            j += 1
            r += 1

    while i < len(other):
        res[r] = other[i]
        i += 1
        r += 1

    while j < len(ten):
        res[r] = ten[j]
        j += 1
        r += 1

    return res


k = 35
arr = [2, 6, 12, 4, 9, 35, 23, 12, 52, -21, -4, 2, 0, 421, -214]
print(arr)
arr = _sort(arr, k)
print(arr)
