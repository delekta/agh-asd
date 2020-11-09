def bubblesort(list):
    for passnum in range(len(list) - 1, 0, -1):
        sorted = True
        for i in range(passnum):
            if list[i] > list[i + 1]:
                sorted = False
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
        if sorted:
            break

list = [2, 5, 45, 4, 67, 34, 9, 34, 453, 3]
list2 = [2, 4, 6, 8, 10]

#checking if break works correctly
bubblesort(list2)

for j in list:
    print(j, " ", end="")

bubblesort(list)
print()

for j in list:
    print(j, " ", end="")
