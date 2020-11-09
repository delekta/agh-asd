# Given two sorted arrays arrX and arrY of size m and n each where m >= n and exactly n
# and arrX has exactly n vacant cells, merge elements of arrY in their correct position
# in array arrX
# Input: arrX = [0, 2, 0, 3, 0, 5, 6, 0, 0]
#        arrY = [1, 8, 9, 10, 15]

def merge_arrays(arrX, arrY, m, n):
    rearrange_array(arrX)
    # last non-zero element
    c = m - n - 1
    for i in range(len(arrY) - 1, -1, -1):
        k = c
        while k >= 0 and arrY[i] < arrX[k]:
            arrX[k + 1] = arrX[k]
            k -= 1

        arrX[k + 1] = arrY[i]
        # last non-zero element is iterated cause we insert one element
        c += 1



# Move all non-zero element in the beginning
def rearrange_array(arrX):
    k = 0
    for i in range(len(arrX)):
        if arrX[i] != 0:
            arrX[k] = arrX[i]
            k += 1

arrX = [0, 2, 0, 3, 0, 5, 6, 0, 0]
arrY = [1, 8, 9, 10, 15]
m = len(arrX)
n = len(arrY)
print(arrX, arrY)
merge_arrays(arrX, arrY, m, n)
print(arrX)