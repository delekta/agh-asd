# (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny,
# wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).
# funkcja: T[i] = min(T[i], T[i - n] + 1) po n -> nominaly


# Time Complexity: O(n * k)
# n -> number of denomination
# k -> amount of money
def number_of_coins(denomination, amount):
    # important preprocessing
    T = [float('inf') for _ in range(amount + 1)]
    T[0] = 0

    for n in denomination:
        for k in range(amount - n + 1):
            if T[k] + 1 < T[k + n]:
                T[k + n] = T[k] + 1

    return T[amount]


# seems to work
def num_of_coins2(denomination, amount):
    T = [float('inf') for _ in range(amount + 1)]
    T[0] = 0

    for i in range(1, amount + 1):
        for n in denomination:
            if n <= i:
                if T[i - n] + 1 < T[i]:
                    T[i] = T[i - n] + 1

    return T[amount]


amount = 15
denomination = [1, 5, 8]

amount2 = 8
denomination2 = [1, 4, 5]

print(num_of_coins2(denomination, amount))
