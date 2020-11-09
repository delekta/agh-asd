# Find largest number possible from set of given numbers. The numbers should be appended
# to each other in any order to form the largest number
# arr = [ 10, 68, 75, 7, 21, 12]

# testing
a = str(15)
b = str(4)
c = int(a + b)
d = int(b + a)
if c > d:
    print(c, "greater than", d)
else:
    print(d, "greater than", c)


def A_greater_b (a, b):
    a = str(a)
    b = str(b)
    c = int(a + b)
    d = int(b + a)
    return c > d


def custom_sort(arr):
    for passnum in range(len(arr) - 1):
        for i in range(len(arr) - passnum - 1):
            if A_greater_b(arr[i], arr[i + 1]):
                arr[i], arr[i + 1], = arr[i + 1], arr[i]


arr = [10, 68, 75, 7, 21, 12]

print(arr)
custom_sort(arr)
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end="")
