# Dana jest posortowana tablica A wielkości n zawierająca parami różne liczby naturalne.
# Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.


# dla unikatowych naturalnych:
def check(A):
    return A[0] == 0


# dla unkatowych calkowitych:
# Skoro tablica jest posortowana, to dla j-tego indeksu:
# jeżeli A[j] < j, to jeżeli istnieje A[i] == i, to musi być na prawo
# jeżeli A[i] > j, to jeżeli istnieje A[i] == i, to musi być na lewo
# Wystarczy więc wykonać przeszukiwanie binarne z decyzją o tym, gdzie przeszukiwać,
# podejmowaną zgodnie z powyższymi zasadami. Złożoność: O(log(n))

# dla nieunikatowych wartosci powyzszy algorytm juz nie dziala
