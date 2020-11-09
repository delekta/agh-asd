# Mamy N * N tablice liczb, ktore moge sie powtarzac i jest ona posortowana, nagle tablica
# zostaje pocieta na N rownych kawalkow. Prosze zaproponowac algorytm do poslejania
# Sort N table by theirs first elements if two has the same first element then by last element


def special_sort(arr_all, n):
    # remember passnum ( n - 1 )
    for passnum in range(n - 1, 0, -1):
        for j in range(passnum):
            if arr_all[j][0] > arr_all[j + 1][0]:
                arr_all[j], arr_all[j + 1] = arr_all[j + 1], arr_all[j]
            elif arr_all[j][0] == arr_all[j + 1][0]:
                if arr_all[j][n - 1] > arr_all[j + 1][n - 1]:
                    arr_all[j], arr_all[j + 1] = arr_all[j + 1], arr_all[j]


def merge(arr_all, n):
    special_sort(arr_all, n)
    new_arr = [0] * n * n
    which_arr = 0
    el = 0
    k = 0
    while which_arr < n:
        new_arr[k] = arr_all[which_arr][el]
        el += 1
        k += 1
        if el == n:
            el = 0
            which_arr += 1
    print(new_arr)


arr = [1, 1, 1, 1, 1, 5, 6, 7, 8, 34, 45, 45, 46, 56, 78, 79] # 16 elements = 4 * 4
arr1 = [1, 1, 1, 1]
arr2 = [1, 5, 6, 7]
arr3 = [8, 34, 45, 45]
arr4 = [46, 56, 78, 79]

arr_all = {0: arr2, 1: arr4, 2: arr3, 3: arr1}
# arr_all = [arr2, arr4, arr3, arr1]

merge(arr_all, len(arr_all))
