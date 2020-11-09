"""
Dana jest tablica (w Pythonie - lista) arr o długości m*n, która zawiera parami różne wartości.
"Pocięto" ją na n kawałków takich samych długości, a następnie losowo poprzestawiano te kawałki.
Następnie elementy w każdym kawałku także losowo poprzestawiano. Napisz funkcję sortUnsorted(arr, n)
"""
# 1. Sort kawalki(kazdy z osobna)
# 2. Posortuj te kawalki wzgledem siebie


# Czy mozna lepiej?
def special_sort(arr_all, n):
    # remember passnum ( n - 1 )
    for passnum in range(n - 1, 0, -1):
        for j in range(passnum):
            if arr_all[j][0] > arr_all[j + 1][0]:
                arr_all[j], arr_all[j + 1] = arr_all[j + 1], arr_all[j]
            elif arr_all[j][0] == arr_all[j + 1][0]:
                if arr_all[j][n - 1] > arr_all[j + 1][n - 1]:
                    arr_all[j], arr_all[j + 1] = arr_all[j + 1], arr_all[j]


def merge(arr_all):

    # Przy zalozeniu ze kazdy kawalek ta sama dlg (length)
    length = len(arr_all[0])
    new_arr = [0] * len(arr_all) * length

    for i in range(len(arr_all)):
        arr_all[i].sort()

    special_sort(arr_all, len(arr_all))

    idx = 0
    for j in range(len(new_arr)):
        new_arr[j] = arr_all[j // length][j % length]

    print(new_arr)

# tabilce ktore powstaly przez pociecie tablicy wyjsciowej, przy zalozeniu ze wyjsciowa byla posortowana
arr1 = [2, 7, 5, 10]
arr2 = [21, 32, 35, 26]
arr3 = [12, 14, 11, 16]
arr4 = [42, 83, 55, 43]
arr_all = [arr4, arr3, arr1, arr2]
merge(arr_all)





