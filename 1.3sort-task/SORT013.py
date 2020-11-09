# Given an unsorted array of integers, find a pair with given sum in it.
# Input: arr = [8, 7, 2, 5, 3, 1]
# sum = 10
# Output: Pair found at index 0 and 2 or Pair found at index 1 and 4
# Idea is to have to indices low and high, sum the val arr[low] and arr[high]
# When sum is greater we decrease high, when is lower we increase low

def sum(arr, sum):
    low = 0
    high = len(arr) - 1
    while low < high:

        if(arr[low] + arr[high] == sum):
            print("Pair found at index", low,"and", high)
            return
        if arr[low] + arr[high] > sum:
            high -= 1
        else:
            low += 1

    print("Pair not found")

suma = int(input("Podaj szukana sume:"))
arr = [8, 7, 2, 5, 3, 1]
arr.sort()
print(arr)
sum(arr, suma)

