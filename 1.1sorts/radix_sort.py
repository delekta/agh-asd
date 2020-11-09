# radix sort - moja wersja


# c -> wg ktorej cyfry sortujemy
def counting_sort(arr, c):
    B = [0 for _ in range(len(arr))]
    C = [0 for _ in range(10)]
    # array of c-th digit
    D = [0 for _ in range(len(arr))]

    for j in range(len(arr)):
        D[j] = get_c_digit(arr[j], c)

    for j in range(len(arr)):
        C[D[j]] += 1

    for j in range(1, 10):
        C[j] += C[j - 1]

    for j in range(len(arr) - 1, -1, -1):
        C[D[j]] -= 1
        B[C[D[j]]] = arr[j]

    # rewriting arr
    for j in range(len(arr)):
        arr[j] = B[j]

    print(arr)


def get_c_digit(num, c):
    if c > digit(num):
        return 0
    else:
        return num % pow(10, c) // pow(10, c - 1)


def digit(num):
    res = 0
    while num > 0:
        res += 1
        # important because num /= 10 didnt work, then if num = 1224, res = 327 :o
        num = num // 10
    return res


def radix_sort(arr):
    maks = max(arr)
    d = digit(maks)
    for c in range(1, d + 1):
        counting_sort(arr, c)


arr = [23, 256, 67, 3, 1224, 7, 40, 222, 59, 22, 11, 1, 45, 13, 1261, 321, 9]
radix_sort(arr)