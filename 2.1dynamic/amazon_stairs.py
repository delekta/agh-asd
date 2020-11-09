# Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji
# 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję. Przykład A={1,3,2,1,0}
# z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile
# sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
# Niech f(i) oznacza na ile sposobow moge przejsc z i na n - 1
# Oczywisicie interesuje nas f(0)
# Time complexity: O(n * max(arr))


def amazon_stairs(arr):
    n = len(arr)
    f = [0] * n

    # its obvious that from n - 2 its only one way
    f[n - 1] = 0
    f[n - 2] = 1

    for i in range(n - 3, -1, -1):
        k = 1
        while k <= arr[i] and i + k <= n - 2:
            f[i] += f[i + k]
            k += 1
        # musi byc
        if i + arr[i] >= n - 1:
            f[i] += 1

    print(f)
    return f[0]


# z algo start
def Staircase(A):
    n = len(A)
    dp = [0] * n  # defaultowo mamy tam wartości 0
    dp[n-2] = 1
    for i in range(n - 3, -1, -1):
        k = 1
        while k <= A[i] and i + k <= n - 1:
            dp[i] += dp[i+k]
            k += 1

    return dp[0]


arr = [1, 3, 2, 1, 0]

print(amazon_stairs(arr))
print(Staircase(arr))
