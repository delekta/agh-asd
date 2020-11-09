def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            #j + 1 and it works perfectly, j and j - 1 almost perfectly
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

list = [2, 5, 45, 4, 67, 34, 9, 34, 453, 3, 78, 543, 11]

for j in list:
    print(j, " ", end="")

insertionsort(list)
print()

for j in list:
    print(j, " ", end="")
