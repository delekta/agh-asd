# Longest increasing subsequence


# Time complexity: O(n^2), its possible to be nlogn
def LIS(arr):
    n = len(arr)
    res = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1

    # important, we must return max of res, actual arr is good example
    print(res)
    return max(res)


arr = [9, 7, 4, 1, 5, 6, 5, 5, 5, 5]
print(LIS(arr))
