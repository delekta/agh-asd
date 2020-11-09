# kth - smallest cormen - version


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[right], arr[i] = arr[i], arr[right]
    return i


def kthsmallest(arr, left, right, k):
    if left == right:
        return arr[left]
    q = partition(arr, left, right)
    print(q, arr)
    size = q - left + 1
    if size == k:   # the pivot value is the answear
        return arr[q]
    if k < size:
        return kthsmallest(arr, left, q - 1, k)
    else:
        return kthsmallest(arr, q + 1, right, k - size)


arr = [3, 4, 1, 8, 2, 6, 9, 10, 5, 7]
print(kthsmallest(arr, 0, len(arr) - 1, 7))
