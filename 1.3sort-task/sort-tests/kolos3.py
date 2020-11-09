#  Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą
#  dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie jak najszybszy.
#  Proszę oszacować jego złożoność obliczeniową.


# 1. Najpierw sortujemy tablice quicksortem O(nlogn)
# 2. Pozniej dla kazdego elementu i ustawiamy dwa wskazniki na pierwszy i ostatni element posortowanej tablicy
# szukana = arr[i]
# 3. Jesli szukana > od arr[first] + arr[last] to inkrementujemy wskaznik first(czyli zwiekszamy sume)
# , gdy szukana < arr[first] + arr[last] to dekrementujemy wskaznik last(czyli zmniejszamy sume)
# 4. Gdy wskazniki sie przetną to zwracam False(czyli nie znalezlismy dla jakiegos)
# 5. Gdy znajde sume to przechodze do nastepnego elementu.
# 6. Gdy wykonam dla wszystkich n to znaczy ze dla kazdej szukanej znalazlem odpowiadajaca sume
#  Zlozonosc: O(n^2) bo dla kazdego elementu szukamy liniowo czy isntnieje dla niego suma w tablicy czyli n * n
