# Three arrays of same size are given. Find a triplet such that maximum - minimum in that thriplet
# of all the triplets. A triplet should be selected in a way such that it should have one number from
# each of three given arrays
# using min - heap instead of min(min(a, b), c)
# min - heap geeks for geeks


def find_the_triplet(arr1, arr2, arr3):
    arr1.sort()
    arr2.sort()
    arr3.sort()

    i, j, k = 0, 0, 0

    min_diff = float("inf")

    while i < len(arr1) and j < len(arr2) and k < len(arr3):

        a, b, c = arr1[i], arr2[j], arr3[k]
        mini = min(a, b, c)
        maks = max(a, b, c)

        if a == mini:
            i += 1
        elif b == mini:
            j += 1
        else:
            k += 1

        diff = maks - mini

        if diff < min_diff:
            min_diff = diff
            res_max = maks
            res_min = mini
            res_mid = a + b + c - mini - maks

    return res_max, res_min, res_mid

arr1 = [1, 10, 13, 20, 25]
arr2 = [3, 7, 11, 16, 19, 36]
arr3 = [6, 15, 25, 33, 56, 76]
print("The triplet:", find_the_triplet(arr1, arr2, arr3))

