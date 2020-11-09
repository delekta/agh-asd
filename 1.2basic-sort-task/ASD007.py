# Podac algorytm zliczajacy ilosc inwersji w podanej tablicy A.
# (tj. ilosc par indeksow i,j ze i < j oraz A[ i ] > A [ j ]
# Zlozonosc nlogn, n^2 O punktow!

# Python 3 program to count inversions in an array

def merge(arr, left, mid, right):
    temp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    c = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            c += (mid - i + 1)
            temp[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    return c


def merge_count(arr, left, right):
    c = 0
    if right > left:
        mid = (left + right) // 2
        c += merge_count(arr, left, mid)
        c += merge_count(arr, mid + 1, right)

        c += merge(arr, left, mid, right)
    return c



# Driver Code
# Given array is
arr = [1, 4, 7, 2, 8, 15, 18, 21, 25]
n = len(arr)
result = merge_count(arr, 0, len(arr) - 1)
print("Number of inversions are", result)



