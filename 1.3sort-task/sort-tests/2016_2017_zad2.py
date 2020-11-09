# Proszę zaimplementować funkcję:
# int SumBetween(int T[], int from, int to, int n);
# Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej tablicy znajdywałyby
# się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że liczby w tablicy T są parami różne
# (ale nie można przyjmować żadnego innego rozkładu danych). Zaimplementowana funkcja powinna być możliwie
# jak najszybsza. Proszę oszacować jej złożoność czasową (oraz bardzo krótko uzasadnić to oszacowanie).


def partition(arr, left, right):

    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


# set idx to his place, time complexity: O(n)
def kth_statistic(arr, idx, left, right):
    q = partition(arr, left, right)

    if idx == q:
        return
    elif idx < q:
        kth_statistic(arr, idx, left, q - 1)
    else:
        kth_statistic(arr, idx, q + 1, right)


# Time complexity: O(n)
def sum_between(arr, _from, _to):
    kth_statistic(arr, _from, 0, len(arr) - 1)
    kth_statistic(arr, _to, 0, len(arr) - 1)
    print(arr)

    sum = 0
    for i in range(_from, _to + 1):
        sum += arr[i]
    return sum


arr = [1, 3, 5, 7, 2, 9, 8, 4, 10, 13, 12, 17, 16, 14, 15, 19, 20, 6, 11, 18]

print(arr)
print("Sum:", sum_between(arr, 16, 18))
