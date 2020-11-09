#Given an array of integers, find the smallest window in array sorting
#which will make the entire array sorted in increasing order

def window(arr):
    max_so_far = arr[0]
    min_so_far = arr[len(arr) - 1]
    last_smaller_than_max = last_bigger_than_min = 0
    for i in range(len(arr)):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        if arr[i] < max_so_far:
            last_smaller_than_max = i

    for j in range(len(arr) - 1, -1, -1):
        if arr[j] < min_so_far:
            min_so_far = arr[j]
        if arr[j] > min_so_far:
            last_bigger_than_min = j

    return last_bigger_than_min, last_smaller_than_max

arr = [1, 4, 5, 8, 5, 6, 7, 9, 12, 8, 13, 15, 17]

print(arr)
j, i = window(arr)
print("window from", j, "to", i)