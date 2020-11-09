def binaryinsertionsort(list):
    for i in range(1, len(list)):
        val = list[i]
        x = binarysearch(list, val, 0, i) + 1
        j = i - 1
        for k in range(i, x, -1):
            list[k] = list[k - 1]
        list[x] = val

#recursive binary search
def binarysearch(list, val, start, end):
    if end - start <= 1:
        if val < list[start]:
            return start - 1
        else:
            return start
    mid = (end + start) // 2
    if val > list[mid]:
        return binarysearch(list, val, mid, end)
    elif val < list[mid]:
        return binarysearch(list, val, start, mid)
    else:
        return mid

list = [2, 5, 45, 4, 67, 34, 9, 34, 453, 3, 78, 543, 11]

for j in list:
    print(j, " ", end="")

binaryinsertionsort(list)
print()

for j in list:
    print(j, " ", end="")