#Given an array consisting of positive and negative integers, segregate them in linear time and constant space.
#Output should print contain all negative numbers followed by all positive numbers

def segragate(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]


arr = [-2, 4, -3, 5, 76, 34, -20, 67, 13, -34, -3]
print(arr)
segragate(arr)
print(arr)