# Given a binary array, sort it in linear time and constant space.
# Output should cantain all zeros followed by all ones


def sort(arr):
    zeros = 0
    l = len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
    for j in range(zeros):
        arr[j] = 0
    for k in range(zeros, l):
        arr[k] = 1


arr = [1, 0 , 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0]

print(arr)
sort(arr)
print(arr)


