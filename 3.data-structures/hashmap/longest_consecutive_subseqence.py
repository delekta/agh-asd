# Problem: Mając na wejściu tablicę liczb naturalnych znaleźć długość najdłuższego podciągu kolejnych liczb
# naturalnych. Algorytm powinien działać w czasie O(n). Przykład: [1,5,3,4,8,10,12,11], odpowiedzią jest 3.
# Ciągiem może być 3,4,5 lub 10,11,12


def LCS(arr):
    res = 0
    s = set(arr)

    for el in arr:
        if el - 1 not in s:

            j = el
            while j in s:
                j += 1

            res = max(res, j - el)

    return res


arr = [1, 5, 3, 4, 8, 10, 12, 11, 6, 9, 13]

print(LCS(arr))

