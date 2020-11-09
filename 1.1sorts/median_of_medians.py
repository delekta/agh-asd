# Median of medians which is useful in partition function(selection, quicksort)
# It make selections algorithm worst case performance O( n )


def find_median(arr, left, x):
    list = []
    for idx in range(left, left + x):
        list.append(arr[idx])
    list.sort()
    return list[x // 2]


def median_of_medians(arr, left, right):
    n = right - left + 1

    median = []
    i = 0
    while i < (n // 5):
        median.append(find_median(arr, i * 5, 5))
        i += 1

    # for last elements
    if i * 5 < n:
        median.append(find_median(arr, i * 5, n % 5))
        i += 1

    if i == 1:
        res = int(median[0])
        return res
    else:
        # There must be "RETURN" cause function return None if not
        return median_of_medians(median, 0, i - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 24, 34, 12, 12, 24, 12, 32, 64, 4, 2, 1, 2, 66, 2]
med = median_of_medians(arr, 0, len(arr) - 1)
print(med)
