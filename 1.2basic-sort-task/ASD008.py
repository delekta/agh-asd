# Given two arrays: arr1[0.. m -1] and arr2[0..n - 1]. Find whether arr2 is a subset of arr1[] or not. Both the arrays
# are not in sorted order. it may be assumed that elements in both array are distinct.

def is_a_subsequence(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(arr1, "\n", arr2)
    i = 0
    while i < len(arr1) and arr1[i] < arr2[0]:
        i += 1
    j = 0
    while j < len(arr2) and arr1[i] == arr2[j]:
        j += 1
        i += 1
    if j == len(arr2):
        print("arr2 is a subsequence of arr1")
    else:
        print("arr2 is NOT a subsequence of arr1")


def is_a_subset(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    while i < len(arr1):
        if j == len(arr2):
            break

        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        else:
            i += 1

    if j == len(arr2):
        print("arr2 is a subset of arr1")
    else:
        print("arr2 is NOT a subset of arr1")


arr1 = [2, 1, 7, 3, 5, 10, 15, 17]
arr2 = [7, 5, 3, 17]

is_a_subsequence(arr1, arr2)
is_a_subset(arr1, arr2)
