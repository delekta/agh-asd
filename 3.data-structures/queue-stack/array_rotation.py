# Proszę podać algorytm “przesuwający” zadaną n-elementową tablicę A o k pozycji. (Przesunięcie
# tablicy oznacza, że element, który był pierwotnie na pozycji i, powinien się znaleźć na pozycję
# n + k (modulo n). Algorytm powinien działać w miejscu


# without auxiliary memory
def rotate1(arr, first, last):
    while first < last:
        arr[first], arr[last] = arr[last], arr[first]
        first += 1
        last -= 1


def array_rotation(arr, k):
    length = len(arr)
    rotate1(arr, 0, length - k - 1)
    rotate1(arr, length - k, length - 1)
    rotate1(arr, 0, length - 1)


k = 4
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print("Before: ", arr)
array_rotation(arr, k)
print("After: ", arr)