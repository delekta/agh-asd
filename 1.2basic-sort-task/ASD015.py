# Given an array of integer values. we need to find the minimum difference between
# maximum and minimum of all possible K - length subsets
# We must find min of ALL POSSIBLE subsets but we know that min will always
# be sub-sequence of sorted-given array because there the diff are the smallest
# Complexity O(nlogn)
def min_diff(arr, k):
    # because if we have k = 3 we need to check 0 and 2
    k -= 1
    arr.sort()
    diff = float("inf")
    for i in range(0, len(arr) - k):
        curr_diff = arr[i + k] -  arr[i]
        if curr_diff < diff:
            diff = curr_diff

    return diff


arr = [1, 4, 6, 8, 9, 12, 15, 18, 24, 33, 36]

print(min_diff(arr, 10))