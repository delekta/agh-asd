#  Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta przyjmuje na wejściu
#  dwie n2-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację elementów z A, że:

# suma od i = 0 do n -1 B[i] < suma od i = n do i = 2n - 1 B[i] < suma od i = n^2 - n do i = n^2 - 1 B[i]
# # czyli posortowac tak ze suma elementow w pierwszym wierzu jest mniejsza niz suma elementow w drugim wierszu itd.

# Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej.
# Proszę oszacować i podać jej złożoność czasową.


def partition(arr, left, right):
    pivot = arr[right][1]
    i = left - 1
    for j in range(left, right):
        if arr[j][1] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort_by_sum(arr, left, right):
    if right > left:
        q = partition(arr, left, right)
        quicksort_by_sum(arr, left, q - 1)
        quicksort_by_sum(arr, q + 1, right)


# Total time complexity: O(n^2)
def sum_sorted(A):
    n = len(A)
    sum_in_row = [0] * n
    B = [[None for _ in range(n)] for _ in range(n)]

    # Time complexity: O(n^2)
    for row in range(n):
        sum = 0
        for column in range(n):
            sum += A[row][column]
        sum_in_row[row] = (row, sum)

    # Time complexity: O(nlogn)
    quicksort_by_sum(sum_in_row, 0, len(sum_in_row) - 1)

    print(sum_in_row)

    row_B = 0
    # Time complexity: O(n^2)
    for i, suma in sum_in_row:
        for j in range(n):
            B[row_B][j] = A[i][j]
        row_B += 1

    print(B)


arr = [
    [1, 2, 4, 7],
    [2, 3, 2, 1],
    [3, 3, 2, 5],
    [2, 3, 5, 1],
]

sum_sorted(arr)
