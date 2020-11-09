#Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formedfrom digitsof the array.
#All digits of given array must be used to form the two numbers.
#Input: [6, 8, 4, 5, 2, 3]
#Output: 604, The minimum sum is formed by numbers 358 and 246
#Input: [5, 3, 0, 7, 4]
#Output: 82, The minimum sum is formed by numbers 35 and 047

def min_sum(arr):
    arr.sort()
    print(arr)
    idx = 0
    #Local variable might be referenced before assignment
    num1 = num2 = 0
    while idx < len(arr):
        num1 = num1 * 10 + arr[idx]
        idx += 1
        if idx < len(arr):
            num2 = num2 * 10 + arr[idx]
        idx += 1

    sum = num1 + num2
    print(sum, "The minimum sum is formed by numbers", num1, "and", num2)

arr1 = [6, 8, 4, 5, 2, 3]
arr2 = [5, 3, 0, 7, 4]

min_sum(arr1)
min_sum(arr2)

