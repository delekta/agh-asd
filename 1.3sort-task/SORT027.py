# Zadanie 6
# Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej, zaledwie
# O(log(n)) liczb jest unikatowe (reszta to powtórzenia). Napisz algorytm, który w czasie O(n*log(log(n)))
# posortuje taką tablicę.
# Pomysl: tworzysz dodatkowa tablice(hashmape) nlogn krotek(element i ilosc), po napotkaniu
# binary search szukasz i jesli element juz jest to dodajesz do ilosci jesli nie to przesuwasz wszystko w prawo i
# wstawiasz na miejsce, na hashmapie łatwiejszy insertion bo nie trzeba przesuwać
# Nie wiadomo jakiej podstawy ten log wiec robimy ze jest 1/3 unikatowych elementow

#if you want good position for insertion  you must leff "<=" right ... return left

#Potrzeba optymailizacji 26.03.2020
def move_and_insert(arr, place, el, last):

    if place == len(arr) - 1 or arr[place][0] == 0:
        arr[place][0] = el
        arr[place][1] = 1

    else:
        j = last
        while j != place:
            arr[j + 1][0] = arr[j][0]
            arr[j + 1][1] = arr[j][1]
            j -= 1

        arr[j + 1][0] = arr[j][0]
        arr[j + 1][1] = arr[j][1]

        arr[place][0] = el
        arr[place][1] = 1


def last_idx(arr):
    i = 0
    if arr[0][0] == 0:
        return 0

    while i < len(arr) and arr[i][0] != 0:
        i += 1
    return i - 1


def insertion_search(arr, left, right, val):
    if right == 0:
        if arr[0][0] == 0:
            return 0
        elif val <= arr[0][0]:
            return 0
        else:
            return 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] == val:
            return mid
        elif val < arr[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    return left


def create_sorted_arr(arr):
    # in tuple you cant change value
    # tak nie rob bo pozniej jak uzupelniasz new_arr[0][0] to uzupelnia cala tablice
    # arr[0][i] ta wartoscia bo ten sam wskaznik
    new_arr = [[0,0] for _ in range(len(arr) // 3)]

    for el in arr:
        last = last_idx(new_arr)
        place = insertion_search(new_arr, 0, last, el)
        if place > last:
            new_arr[place][0] = el
            new_arr[place][1] += 1
        elif el == new_arr[place][0]:
            new_arr[place][1] += 1
        else:
            move_and_insert(new_arr, place, el, last)

    print(new_arr)


arr = [7, 2, 2, 3, 12, 7, 2, 2, 3, 12, 12, 2, 9, 3, 7]

create_sorted_arr(arr)
