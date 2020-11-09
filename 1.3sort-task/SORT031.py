# Zadanie 10
# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. Proszę napisać
# algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich GCD jest różny od 1.
# Algorytm powinien działać jak najszybciej.
# GCD - greatest common divisor (najwiekszy wspolny dzielnik)
# Nie ma to za wiele zwiazane z sortowaniem
# Pomysl: Należy przygotować tablicę o rozmiarze n. Następnie dla kązdej liczby iterować po
# wartościcach od 2 do sqrt(liczba) i inkrementować występienia odpowiednich dzielników w
# tablicy pomocniczej. największa wartość w tablicy pomocniczej jest rozwiązaniem.
from math import sqrt


def greatest_subset(arr, n):
    factors = [0 for _ in range(n + 1)]

    for el in arr:
        for i in range(2, int(sqrt(el)) + 1):
            if el % i == 0:
                factors[i] += 1
        # musi byc
        factors[el] += 1

    max = -float('inf')
    for i in range(n + 1):
        if factors[i] > max:
            max = factors[i]
            ans = i

    return ans


arr = [1, 4, 2, 3, 2, 4, 4, 8, 7, 5]
print(greatest_subset(arr, len(arr)))

