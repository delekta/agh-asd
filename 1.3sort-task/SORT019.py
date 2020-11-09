# Comparison Quick Sort vs Radix Sort
# Nalzey posortowac N liczb K-cyfrowych reprezentowanych jako napis:
# Prosze porownac dwie metody:
# - Quick Sort
# - Radix Sort
# Dla jakich K i N sortowanie pozycyjne bedzie lepsze?
import random
import time


def generate_N_element_array_of_K_digits(n, k):
    random.seed(time.time())
    arr = [str(random.randrange(pow(10, k - 1), pow(10, k))) for _ in range(n)]

    # for el in arr:
    #    print(el[0], el)

    return arr


def random_partition(arr, left, right):
    x = random.randint(left, right)
    arr[x], arr[right] = arr[right], arr[x]
    return partition(arr, left, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksort(arr, left, right):
    if right > left:
        p = random_partition(arr, left,right)
        quicksort(arr, left, p - 1)
        quicksort(arr, p + 1, right)


# k = 10 beacause 10 digits
# which digits d
def counting_sort(A, k, d):
    B = [0] * len(A)
    C = [0] * k

    for i in range(len(A)):
        C[int(A[i][d])] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[int(A[i][d])] -= 1
        B[C[int(A[i][d])]] = A[i]

    # return didnt work hmmm...
    for i in range(len(A)):
        A[i] = B[i]


# k digits
def radix_sort(arr, k):
    for d in range(k - 1, -1, -1):
        counting_sort(arr, 10, d)


# Radix is faster when k is small
# When k is large Quick sort much faster
n = 1000
k = 32
arr_radix = generate_N_element_array_of_K_digits(n, k)

# list slicing the fastest copying
arr_quick = arr_radix[:]

# sting[i][ k - 1] is last number
# print(arr_radix[0][ k - 1])

print("Radix sort:")
# print(arr_radix)
tic_radix = time.perf_counter()
radix_sort(arr_radix, k)
tac_radix = time.perf_counter()
result_radix = tac_radix - tic_radix
print(result_radix)
# print(arr_radix)

print()

print("Quick sort:")
# print(arr_quick)
tic_quick = time.perf_counter()
quicksort(arr_quick, 0, len(arr_quick) - 1)
tac_quick = time.perf_counter()
result_quick = tac_quick - tic_quick
print(result_quick)
# print(arr_quick)

if result_radix < result_quick:
    print("Radix is faster")
else:
    print("Quick is faster")

# When you use Quick Sort ?
# When you don't need a stable sort and average case performance matters more than worst case performance.
# A quick sort is O(N log N) on average, O(N^2) in the worst case. A good implementation uses O(log N)
# auxiliary storage in the form of stack space for recursion.

# When you use Radix Sort?
# When log(N) is significantly larger than K, where K is the number of radix digits.
