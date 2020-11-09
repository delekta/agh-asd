# Sortowania liniowe
# Zadanie 3
# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
# czy w tablicy ponad połowa elementów ma jednakową wartość.
# Pomysl: algorytmem kthstatistic(statystyka pozycyjna) szukamy arr[n / 2] i przechodzac
# po tablicy sprawdzamy czy jest ponad polowa tego elementu. Counting Sort nie!!!
# Mozna jeszcze Bucket Sort z rozmiarem polowy tablicy
# Drugi sposob: Bucket sort, ale trzymamy także informację o wielkości każdego kubełka - kiedy dodanie kolejnego
# elementu sprawi, że dany kubełek będzie rozmiaru przynajmniej n/2, to zwracamy True.


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def kth_statistic(arr, left, right, k):
    if left == right:
        return arr[left]

    pi = partition(arr, left, right)

    size = pi - left + 1
    if size == k:
        return arr[pi]
    elif k < size:
        return kth_statistic(arr, left, pi - 1, k)
    else:
        return kth_statistic(arr, pi + 1, right, k - size)


def half_of_elements(arr):
    val = kth_statistic(arr, 0, len(arr) - 1, len(arr) // 2)
    length = len(arr)
    counter = 0
    for el in arr:
        if el == val:
            counter += 1
        if counter == (length // 2 + 1):
            return True

    return False


arr = [1, 2, 2, 2, 4, 2, 4, 2, 7, 1]
print(half_of_elements(arr))
