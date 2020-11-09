# My Bucket Sort


# insertion sort is good sorting algorithm to use if the input list is already mostly sorted
def insertion_sort(arr):
    # you must take last element len(arr) !!!
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        # you must compare with key cause arr[i] is changing
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Note arr values belong 0.0 .. 1.0
def bucket_sort(arr, k):
    buckets = [[] for _ in range(k)]

    for el in arr:
        # buckets[].append !!!
        # should  be k - 1 cause if el = 1 int(el * k) = len(buckets) = k = error
        buckets[int(el * (k - 1))].append(el)

    res = []
    for i in range(k):
        insertion_sort(buckets[i])
        # traditionally in two separate loop
        res.extend(buckets[i])

    # rewriting array
    for i in range(len(arr)):
        arr[i] = res[i]


# Arr values belong to 0.0 .. inf
def bucket_sort_normalized(arr2, k):
    maks = max(arr2)
    tmp = [0 for _ in range(k)]
    buckets = [[] for _ in range(k)]
    for i in range(k):
        # tmp values belong 0.0 .. 1.0
        tmp[i] = arr2[i] / maks

    for i in range(k):
        # buckets[].append
        # must be k - 1 because for maks tmp[i] = 1 and k is a len(arr2), so we have buckets[len(arr2)]
        buckets[int(tmp[i] * (k - 1))].append(arr2[i])

    res = []
    for i in range(k):
        insertion_sort(buckets[i])
        res.extend(buckets[i])

    for i in range(k):
        arr2[i] = res[i]

print("Sorting array 0.0 .. 1.0")
arr = [0.923, 0.953, 0.421, 0.42, 0.1, 0.23, 0.39, 0.84, 0.73, 1.0, 0.343, 0.542, 0.6, 0.532, 0.763, 0.02]
print(arr)
bucket_sort(arr, len(arr))
print(arr)

print("Sorting array 0.0 .. inf")
arr2 = [7.5, 33.21, 15.23, 75.3, 43, 32.4, 21.8, 21.5, 74.2, 96.7, 62.123, 84.1, 21.87, 53.2, 88.3, 0.32]
print(arr2)
bucket_sort_normalized(arr2, len(arr2))
print(arr2)
