# Given an array containing only 0's, 1's, 2's, sort the array in linear time and using constant space
# Simple solution would be to perform count sort. We count the number of 0's, 1's and 2's and then
# put them in the array in corrrect order. The time complexity of above solution is O(n) but it requires two traversal
# we can rearrange the array in the single traversal using an alternative linear-time partition routine can be used
# that seperates the values into three groups, values less than pivot, values equal to the pivot, greater than the pivot

def threeWayPartition(arr):
    end = len(arr) - 1
    start = 0
    mid = 0
    pivot = 1
    while mid <= end:

        if arr[mid] < pivot:
            arr[mid], arr[start] = arr[start], arr[mid]
            mid += 1
            start += 1
        elif arr[mid] > pivot:
            arr[mid], arr[end] = arr[end], arr[mid]
            # mid += 1 because when you swap with end you dont know what is there so you must check it
            # in arr[mid] < pivot you know that you swap 0 with 1
            end -= 1
        else:
            mid += 1


arr = [1, 0, 2, 2, 0, 0, 1, 1, 2, 0, 1, 2, 1, 2, 2, 0]

print(arr)
threeWayPartition(arr)
print(arr)
