# Sortowania liniowe
# Zadanie 2
# Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n.
# Napisz algorytm, który posortuje tę tablicę w czasie O(n).
# Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
# Uwagi: najpierw sortujemy po dlugosciach, pozniej po alfabecie, czyli bb < aaa
# Jest druga wersja tego zadania
# Pomysl: Najpierw dzielimy bucket sortem na słowa tej samej długosci(n bucketow), a potem radixem kazdy backet
# Mozna tez zrobic krotki (len(napis), napis)

def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]

    for el in arr:
        buckets[len(el)].append(el)

    res = []
    for i in range(len(buckets)):
        # i is length of word in bucket
        radix_sort(buckets[i], i)
        res.extend(buckets[i])

    for i in range(len(arr)):
        arr[i] = res[i]


# Trying if order of functions in python matter
def radix_sort(bucket, length):
    for d in range(length - 1, -1, -1):
        counting_sort(bucket, d)


def counting_sort(A, d):
    B = [0] * len(A)
    # english alphabet has 26 characters
    C = [0] * 26

    for i in range(len(A)):
        C[ord(A[i][d]) - 97] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[ord(A[i][d]) - 97] -= 1
        B[C[ord(A[i][d]) - 97]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


arr = ['aba', 'bbb', 'cas', 'caa', 'bba', 'z', 't', 'd', 'ac', 'as', 'ba', 'xa', 'dq', 'qdzz', 'axx', 'adda', 'bbbb', 'azzz']

# Checking if radix sort works
# print(arr)
# radix_sort(arr, 3)
# print(arr)

print(arr)
bucket_sort(arr)
print(arr)