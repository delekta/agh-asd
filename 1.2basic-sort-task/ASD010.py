# Given an array arr[0.. n - 1] of distinct elements and a range [low, high], find all
# that are in range, but not in array. The missing elements should be printes in sorted order


def binary_upper_bound(x, Y, l, r):
    while r >= l:
        mid = (l + r) // 2
        if Y[mid] == x:
            return mid
        if Y[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return l


def in_range(arr, low, high):
    arr.sort()
    idx = 0

    # while arr[idx] < low:
    #     idx += 1

    # binary search faster than while loop
    idx = binary_upper_bound(low, arr, 0, len(arr) - 1)

    while idx < len(arr) and arr[idx] <= high:
        if low < arr[idx]:
            print(low, end=" ")
        else:
            idx += 1
        low += 1

    while low <= high:
        print(low, end=" ")
        low += 1


arr = [1, 3, 5, 3, 9, 1, 13, 15, 17]

in_range(arr, 7, 13)
