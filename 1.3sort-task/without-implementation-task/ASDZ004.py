#  Proszę podać możliwie jak najszybszy algorytm sortujący tablicę A liczb wymiernych.
#  Tablica A zawiera tylko log(n) różnych wartości (gdzie n to długość tablicy A)

"""
1 Sposob:
Rozwiązanie: Tu możliwe są różne warianty. Najbardziej oczywisty i zaproponowany przez większość uczestników polega
na tym, że konstruujemy posortowaną tablicę krotek (powiedzmy B), gdzie pierwszy element to wartość, a drugi to
liczba jej wystąpień w tablicy A. Skanujemy A i dla każdego elementu szukamy jego odpowiednika w B, stosując
wyszukiwanie binarne. Jak nie znajdziemy, qw B danej liczby to dodajemy ją do B, a jak znajdziemy – zwiększamy
licznik liczby wystąpień. W pierwszym przypadku wyszukiwanie ma złożoność O(log(length(B))), czyli O(log log n).
W drugim – szereg elementów trzeba przesunąć, ale skoro takich przesunięć nie może być więcej niż logn, to ogólna
 złożoność tej części nadal wynosi O (n log log n) (łączny koszt przesunięć to O(log^2n).

2. Sposob:
Podobny efekt można uzyskać za pomocą innych struktur danych, takich jak np. drzewa czerwonoczarne albo AVL
 (generalnie chodzi o to żeby można było w takich strukturach wyszukać element w czasie logarytmicznym).
 Ale na wykładach takich struktur jeszcze nie było.

3. Sposob:
 Inne możliwe podejście mogłoby polegać na zastosowaniu algorytmu QuickerSort (wersji QuickSort gdzie dzielimy tablicę
na mniejsze od pivota, równe pivotowi i większe od pivota). Algorytm zagłębi się rekurencyjnie tylko na loglogn
poziomów, co daje złożoność O(nloglogn) (zakładając, że będziemy mieli dobre wybory pivotów).

"""