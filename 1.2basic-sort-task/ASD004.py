#Given an integer array, find a maximum product of triplet in array
#Input: [ 10, 3, 5, 6, 20 ]
#Output: 1200, Multiplication of 10, 6 and 20
#Input: [ -10, -3, -5, -6,-20 ]
#Output: -90

def max_product_of_tiplet(arr):
    arr.sort()
    print(arr)
    n = len(arr)

    a1 = [ arr[n - 1], arr[n -2], arr[n -3] ]
    a2 = [ arr[n - 1], arr[0], arr[1] ]

    product1 = a1[0] * a1[1] * a1[2]
    product2 = a2[0] * a2[1] * a2[2]

    if  product1 >= product2:
        print(product1, ", Multiplication of:", a1[0], a1[1], a1[2])
    else:
        print(product2, ", Multiplication of:", a2[0], a2[1], a2[2])

arr1 = [ 10, 3, 5, 6, 20 ]
arr2 = [ -10, -3, -5, -6, -20, 1]

max_product_of_tiplet(arr1)
max_product_of_tiplet(arr2)

