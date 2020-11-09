#Given an array, find the number of inversions of it. If ( i < j ) and ( A[i] > A[j]) then the pair (i, j)
#is called an inversion of the array. We need to count all such pairs in the array

def count_inversions(arr):
    counter = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                counter += 1
    return counter

arr = [1, 3, 9, 6, 8, 91, 90, 102]
count = count_inversions(arr)
print(count)