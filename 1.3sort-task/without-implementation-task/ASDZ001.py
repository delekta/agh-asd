"""Dana jest n-elementowa tablica A zawierająca liczby naturalne
(potencjalnie bardzo duże). Wiadomo, że tablica A powstała w dwóch
 krokach. Najpierw wygenerowano losowo (z nieznanym rozkładem) n
różnych liczb nieparzystych i posortowano je rosnąco. Następnie
wybrano losowo ceil(log n) elementów powstałej tablicy i zamieniono
je na losowo wybrane liczby parzyste. Zaproponuj (bez implementacji!)
algorytm sortowania tak powstałych danych. Algorytm powinien być
możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową. """
# complexity of building heap is O( n )
# len_even = ceil(logN)
"""Przechodzimy po tablicy i wrzucamy liczby parzyste do osobnej tablicy, zastepujac je np '-1'
sortujemy te tablice, zajmuje log(n) * log(log(n)), przejscie to O(n), pozniej mamy 2 posortowane
tablice: nieparzystych ( z dziurami tam gdzie byly parzyste) i parzystych, robimy kolejna tablice 
dlugosci n, reszta sprowadza sie do sklejenia dwoch tablic, oczywiscie jest tu zlozonosc pamieciowa
O( n + logn) ale o pamieci nikt nic nie mowil"""

# dodatkowa implementacja
# nigdzie nie ma mowy o pamieci wiec zuzywamy jej wiecej zeby zyskac na szybkosci
def sort_odd_even(arr):
    # rewrite even number
    arr_even = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr_even.append(arr[i])
            arr[i] = -1
    # we presume that this is nlogn (e.g quicksort)
    arr_even.sort()
    arr_res = [0] * len(arr)
    i = 0
    j = 0
    r = 0
    while i < len(arr) and j < len(arr_even):
        if arr[i] != -1:
            if arr[i] < arr_even[j]:
                arr_res[r] = arr[i]
                r += 1
                i += 1
            else:
                arr_res[r] = arr_even[j]
                r += 1
                j += 1
        else:
            i += 1

    while i < len(arr):
        arr_res[r] = arr[i]
        r += 1
        i += 1
    while j < len(arr_even):
        arr_res[r] = arr_even[j]
        r += 1
        j += 1

    for k in range(len(arr)):
        arr[k] = arr_res[k]
    # complexity O(n + klogk) where k is logn


arr = [1, 3, 5, 7, 9, 2, 17, 48, 25, 29, 33, 39]
sort_odd_even(arr)
print(arr)