# Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej długości.
# Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego(26 znakow)

"""
Rozwiązanie: Najpierw sortujemy wyrazy po długości (przez zliczanie). Następnie sortujemy wyrazy pozycyjnie
z tą poprawką, że dla każdej pozycji 'i' znamy 'k' takie, że tab[:k] zawiera wyrazy krótsze od 'i'.
I na pozycji 'i' sortujemy jedynie fragment tab[k:]. Gdy wyrazy są posortowane po długościach, to
indeksy 'i' możemy wyznaczyć w czasie O(długość najdłuższego słowa). Całość działa, bo w sortowaniu
pozycyjnym używamy sortowania stabilnego.

"""


def partition(arr, left, right):
    pivot = len(arr[right])
    i = left
    for j in range(left, right):
        if len(arr[j]) <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksort_by_length(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort_by_length(arr, left, q - 1)
        quicksort_by_length(arr, q + 1, right)


def find_max_len(arr):
    maks = 0
    for word in arr:
        if len(word) > maks:
            maks = len(word)

    return maks


def find_k_for_poz(arr, maks):
    k_for_poz = [0] * maks
    poz = len(arr[0]) - 1

    for k in range(1, len(arr)):
        if len(arr[k]) > len(arr[k - 1]):
            k_for_poz[len(arr[k]) - 1] = k

    # musimy wypelniac od konca, poniewaz jesli mamy zmiane dlugosci słow z 10, na 12 to dla sortowania pozycji 11
    # wpiszemy k i to samo k powinno byc dla sortowania pozycji 10
    # przepisujemy do i = len(word[0])
    for i in range(maks - 1, len(arr[0]), -1):
        if k_for_poz[i] != 0 and k_for_poz[i - 1] == 0:
            k_for_poz[i - 1] = k_for_poz[i]

    return k_for_poz


# r -> range
def counting_sort(A, r, digit, k):
    B = [0] * len(A)
    # Przesuniecie tablicy C jest nie potrzebne!!!
    # Wystarczy przesunać B w etapie koncowym
    C = [0] * r
    for i in range(k, len(A)):
        # print(A[i][digit])
        idx = ord(A[i][digit]) - 97
        C[idx] += 1
    for j in range(1, r):
        C[j] += C[j - 1]

    # we must take elements from the end to make counting sort stable
    for j in range(len(A) - 1, k - 1, -1):  # k - 1!
        idx = ord(A[j][digit]) - 97
        C[idx] -= 1    # sum of prefix elements
        B[C[idx] + k] = A[j]

    for j in range(k, len(A)):
        A[j] = B[j]


def radix_sort(arr):
    quicksort_by_length(arr, 0, len(arr) - 1)
    maks = find_max_len(arr)
    k_for_poz = find_k_for_poz(arr, maks)

    # radix sort sholud sort from low-order-digit to high-order-digit
    for digit in range(maks - 1, -1, -1):
        k = k_for_poz[digit]
        counting_sort(arr, 26, digit, k)


arr = ["doctor", "allocate", "conclude", "coordinate", "coordination", "clarify", "accord", "arrange", "conform", "aa", "b", "acydol"]

print(arr)
radix_sort(arr)
print(arr)

