def merge(arr, start, mid, end):

    temp = [0] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        # so that you favor left-half values over right-half values, if they are equal
        # it makes algorithm stable (<"=")
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1
    # really important
    for i in range(start, end + 1):
        arr[i] = temp[i - start]


def mergeSort(arr, start, end):
    if end > start:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)

        merge(arr, start, mid, end)


arr = [1, 13, 24, 2, 7, 35, 78, 45, 24, 90, 12, 11, 42]

print(arr)
mergeSort(arr, 0, len(arr) - 1)
print(arr)
