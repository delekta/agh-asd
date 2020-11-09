# Given an array od distinct n integers. The task is to check whether reversing one sub-array make the array sorted
# or not. If the array is already sorted or reversing a subarray once make it sorted, print "Yes", else print "No".
# when we find more than one bump, we cant make array sorted by reversing one subarray


def partition(arr, l, r):
    pivot = arr[r]
    # important i = left, no 0
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def quick_sort(arr, left, right):
    # if you have recursive you sholud have if
    if right > left:
        q = partition(arr, left, right)
        quick_sort(arr, left, q - 1)
        quick_sort(arr, q + 1, right)

def reverse_subarray(arr):
    idx = 1
    length = len(arr)
    while idx < length and arr[idx - 1] < arr[idx]:
        idx += 1

    start = idx - 1

    while idx < length and arr[idx - 1] > arr[idx]:
        idx += 1

    end = idx - 1

    while idx < length and arr[idx - 1] < arr[idx]:
        idx += 1
    print(idx, length, start, end)
    quick_sort(arr, start, end)
    print(arr)

    if idx == length:
        print("Yes")
    else:
        print("No")


arr = [1, 2, 3, 4, 5, 9, 8, 7, 11, 12, 13, 16]
reverse_subarray(arr)