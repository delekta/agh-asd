# In Activity Selection Problem, we are given a set of activities and the starting
# & finishing time each of activity, we need to find the maximum number of activities
# that can be performed by a single person assuming that a person can only work on
# a single activity at a time.
# Input: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
# Output: (1, 4), (5, 7), (8, 11), (12, 14)
# Note: Using greedy approach will always result in an optimal solution to this problem

# We initially sorts the activities in increaasing order of their finish times
def special_sort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i][1] > arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def searching(arr):
    result = [arr[0]]
    for i in range(len(arr) - 1):
        n = len(result) - 1
        if result[n][1] < arr[i + 1][0]:
            result.append(arr[i + 1])

    return result


arr = [(12, 14), (1, 4), (0, 6), (3, 5), (5, 7), (3, 8), (5, 9), (8, 11), (6, 10), (8, 12), (2, 13)]

print(arr)
special_sort(arr)
print(arr)
result = searching(arr)
print(result)