# Longest increasing  subsequence (nlogn)


# finding position for replacing
def binary_search(arr, left, right, searched):
    while right >= left:
        mid = (right + left) // 2
        if arr[mid] == searched:
            return mid
        elif arr[mid] > searched:
            right = mid - 1
        elif arr[mid] < searched:
            left = mid + 1

    # print("Searched:", searched, "left:", left, "right", right)
    return left


def LIS(arr):
    list_of_tails = [0 for _ in range(len(arr))]

    # always points empty slots
    length = 0

    list_of_tails[0] = arr[0]
    length += 1

    for el in arr:
        if el < list_of_tails[0]:
            list_of_tails[0] = el
        elif el > list_of_tails[length - 1]:
            list_of_tails[length] = el
            length += 1
        else:
            idx = binary_search(list_of_tails, 0, length - 1, el)
            list_of_tails[idx] = el

    return length


arr = [0, 8, 4, 1, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(arr))


# binary search test
binary_search_test = [2, 4, 6, 7, 8, 10, 12, 13, 14]

binary_search(binary_search_test, 0, len(binary_search_test) - 1, 1)
binary_search(binary_search_test, 0, len(binary_search_test) - 1, 3)
binary_search(binary_search_test, 0, len(binary_search_test) - 1, 5)
binary_search(binary_search_test, 0, len(binary_search_test) - 1, 9)
binary_search(binary_search_test, 0, len(binary_search_test) - 1, 11)
binary_search(binary_search_test, 0, len(binary_search_test) - 1, 15)

# Conclusion: when we have right >= left
# If we search for element that is not included in array, at the end
# right points the greatest element which is smaller than searched
# left point the smallest element which is bigger than searched



