# Given an array of integers, move all zeros present in the array to the end.
# The solution should maintain the relative order of items in the array

# Sth like counting sort
def movezeros(arr):
    # index of current number
    k = 0
    length = len(arr)
    for i in range(length):
        if arr[i] != 0:
            arr[k] = arr[i]
            k += 1
    for j in range(k, length):
        arr[j] = 0


arr = [1, 2, 0, 3, 0, 4, 5, 0, 0, 7]

print(arr)
movezeros(arr)
print(arr)
