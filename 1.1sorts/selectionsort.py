
#first
def selectionsort(list):
    for i in range(len(list) - 1, 0, -1):
        j = 0
        #must be i + 1
        for k in range(i + 1):
            if list[k] > list[j]:
                j = k
        temp = list[j]
        list[j] = list[i]
        list[i] = temp

#second
def selectionsort2(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[min_idx], list[i] = list[i], list[min_idx]

#third
def stableselectionsort(list):
    for i in range(len(list)):
        min_idx = i
        #finding minimum
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        #move minimum element at current i
        #key is a value of min_idx, it must be like that, cause then you change min_idx
        key = list[min_idx]
        while min_idx > i:
            list[min_idx] = list[min_idx - 1]
            min_idx -= 1
        #key is a value of min_element
        list[i] = key


list = [2, 5, 45, 4, 67, 34, 9, 34, 453, 3, 78, 543, 11]

for j in list:
    print(j, " ", end="")

stableselectionsort(list)
print()

for j in list:
    print(j, " ", end="")

