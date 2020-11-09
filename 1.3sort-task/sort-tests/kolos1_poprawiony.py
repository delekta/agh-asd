#  Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka,
#  która w liczbie występuje więcej niż jeden raz. Mówimy, żeliczbanaturalna A jestładniejszaodliczbynaturalnej
#  B jeżeliwliczbie A występujewięcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to
#  ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455,
#  liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne. Dana jest tablica T zawierająca
#  liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T) która sortuje elementy tablicy T od najładniejszych
#  do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy
#  opis algorytmu oraz proszę oszacować jego złożoność czasową.


def counting_sort_increasing(A, which, r=10):
    B = [0] * len(A)
    C = [0] * r
    for i in range(len(A)):
        C[A[i][which]] += 1
    for j in range(1, len(C)):
        C[j] += C[j - 1]
        # we must take elements from the end to make counting sort stable
    for k in range(len(A) - 1, -1, -1):
        C[A[k][which]] -= 1  # sum of prefix elements
        B[C[A[k][which]]] = A[k]

    for i in range(len(A)):
        A[i] = B[i]


def counting_sort_decreasing(A, which, r=10):
    B = [None for _ in range(len(A))]
    C = [0] * r
    for i in range(len(A)):
        C[A[i][which]] += 1
    for i in range(r - 1, 0, -1):
        C[i - 1] += C[i]

    for i in range(len(A) - 1, -1, -1):
        C[A[i][which]] -= 1
        B[C[A[i][which]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


# Liczy ilosc cyfr wielokrotnych i jednokrotnych
def count(val, arr):
    tmp = val
    for i in range(len(arr)):
        arr[i] = 0

    while val > 0:
        arr[val % 10] += 1
        val //= 10

    num_j = 0
    num_w = 0
    for element in arr:
        if element == 1:
            num_j += 1
        if element > 1:
            num_w += 1
    print(tmp, num_j, num_w)
    return num_j, num_w


def preety_sort(T):
    arr = [0] * 10

    for i in range(len(T)):
        num_j, num_w = count(T[i], arr)
        T[i] = (T[i], num_j, num_w)

    # which = 2 posortuj bo wielokrotnych
    # which = 1 posortuj po jednokrotnych

    # Najpierw posortuje po wielokrotnych rosnaco,
    # Póżniej po jednokrotnych malejaco

    which = 2
    counting_sort_increasing(T, which)  # sortowanie stabilne !!!

    which = 1
    counting_sort_decreasing(T, which)

    for i in range(len(T)):
        T[i] = T[i][0]


T = [455, 122334455, 123466778899,1266, 114577, 13445566,2344, 123, 76333,1357]
preety_sort(T)
print(T)
