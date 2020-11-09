# Given n integers, we need to find size of the largest subset with GCD equal to 1.
# GCD - greatest common divisor


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# two option all array is largest subset with gcd 1, or that subset didnt exist
# if exist subset with gcd 1 if we add element subset still has gcd 1
def largest_gcd_one(arr, n):
    current_gcd = arr[0]
    for i in range(1, n):
        current_gcd = gcd(current_gcd, arr[i])
        if current_gcd == 1:
            return n
    return 0

arr = [2, 6, 14, 4]
print(largest_gcd_one(arr, len(arr)))