# Dana jest tablica zawierająca liczby naturalne. Proszę zaimplementować funkcję odpowiadającą
# na pytanie czy w tablicy jest para sumująca się do jakiejś liczby x. Funkcja powinna być jak najszybsza.
# findPair(arr, x) -> bool.


# Przyklad liniowego znajdowania sumy bez uzywania sortowania
def findPair(arr, x):
    s = set()
    for i in range(len(arr)):
        temp = x - arr[i]
        if temp in s:
            return True
        else:
            s.add(arr[i])
    return False

arr = [6, 3, 6, 2, 23, 66, 1, 73,]
print(arr)
x = 120
print(x, findPair(arr, x))
z = 89
print(z, findPair(arr, z))
