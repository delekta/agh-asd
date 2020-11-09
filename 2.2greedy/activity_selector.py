# Problem wyboru zajęć


# sort by finish time of activities
def special_sort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i][1] > arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# we assign first activity before function
def recursive_selector(arr, length, last, activities):
    j = last + 1
    while j < length and arr[j][0] < arr[last][1]:
        j += 1

    if j < length:
        activities.append(arr[j])
        return recursive_selector(arr, length, j, activities)
    else:
        return activities


# we assign first activity before function
def iterative_selector(arr, length, activities):
    last = 0
    j = last + 1
    while j < length:
        if arr[j][0] >= arr[last][1]:
            activities.append(arr[j])
            last = j
        j += 1
    return activities


def selector(arr):
    length = len(arr)
    special_sort(arr)
    activities1 = [arr[0]]
    activities2 = [arr[0]]
    print(recursive_selector(arr, length, 0, activities1))
    print(iterative_selector(arr, length, activities2))


arr = [(12, 14), (1, 4), (0, 6), (3, 5), (5, 7), (3, 8), (5, 9), (8, 11), (6, 10), (8, 12), (2, 13)]
selector(arr)
