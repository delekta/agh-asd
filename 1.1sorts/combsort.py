def combsort(arr):
    n = len(arr)
    gap = n
    swapped = True
    # while ends when gap == 1 and sort = True
    while swapped or gap > 1 :
        gap = int(gap // 1.3)
        swapped = False
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[gap + i]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

arr = [3, 5, 13, 2, -3, 90, 45, 23, 18, 76, 11]
print(arr)
combsort(arr)
print(arr)