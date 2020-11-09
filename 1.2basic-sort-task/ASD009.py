# Given two arrays X[] and Y[] of possitive integers, find number of pairs such that x^y > y^x
# where x is from X[] and Y[] is an element form Y[]


def binary_upper_bound(x, Y, l, r):
    while r >= l:
        mid = (l + r) // 2
        if Y[mid] == x:
            return mid + 1
        if Y[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return l


def count_aux(x, Y, E):
    ans = 0
    if x == 0:
        return 0
    if x == 1:
        return E[0]
    idx = binary_upper_bound(x, Y, 0, len(Y) - 1)
    ans += len(Y) - idx

    # now we know that x > 0 and x > 1

    ans += E[0] + E[1]
    if x == 2:
        ans -= E[3] + E[4]
    elif x == 3:
        ans += E[2]

    return ans


def count(X, Y):
    Y.sort()
    Exceptions = [0] * 5
    counter = 0
    for i in range(len(Y)):
        if Y[i] < 5:
            Exceptions[Y[i]] += 1

    for i in range(len(X)):
        counter += count_aux(X[i], Y, Exceptions)

    return counter


X = [10, 19, 18]
Y = [11, 15, 9]
c = count(X, Y)
print("Number of pairs: ", c)