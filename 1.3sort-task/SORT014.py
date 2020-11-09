# Merge two sorted array in place, without using any other data structure
# Given two sorted arrays arr1 and arr2 of size m an n each, merge elements of arr1 with elements of array arr2
# by maintaining the sorted order, fill arr1 with first m smallest elements and fill arr2 with remaining elements
# Input: arr1 = [1, 4, 7, 8, 10]
#        arr2 = [2, 3, 9]
# Output arr1 = [1, 2, 3, 4, 7]
#        arr2 = [8, 9, 10]

def merge_arrays(arr1, arr2):
    for i in range(len(arr1)):

        if arr2[0] < arr1[i]:
            arr1[i], arr2[0] = arr2[0], arr1[i]

        first = arr2[0]
        k = 1
        # Remember k < len(arr2)
        while k < len(arr2) and arr2[k] < first:
            arr2[k - 1] = arr2[k]
            k += 1

        arr2[k - 1] = first


arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
print(arr1, arr2)
merge_arrays(arr1, arr2)
print(arr1, arr2)
