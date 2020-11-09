#Check if any two interwals overlap among a given set of intervals. An interval is represented as a combination of
#start line and end line. Given a set of intervals, check if any two intervals overlp.
#Input: arr = [ (1, 3), (5, 7), (2, 4), (6, 8) ]
#Output: The intervals (1, 3) and (2, 4) overlap.

def specialsort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i][0] > arr[i + 1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def ifoverlap(arr):
    specialsort(arr)
    print(arr)
    overlap = False
    idx = 0
    while (not (overlap) and idx < len(arr) - 1):
        overlap = (arr[idx][1] > arr[idx + 1][0])
        idx += 1
    if overlap:
        overlapped = (arr[idx -1], arr[idx])
        print(overlapped, "are overlapped")
    else:
        print("The intervals are not ovelapped")

arr = [ (1, 3), (5, 7), (3, 4), (6, 8) ]

ifoverlap(arr)