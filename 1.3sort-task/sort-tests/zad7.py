# Dana jest nieposortowana tablica A. Należy znaleźć maksymalną różnicę pomiędzy
# kolejnymi elementami w porządku posortowanym. Zadanie należy rozwiązać w czasie liniowym. 

# 1. Najpierw znajdujemy minimum i maksimum w A (w czasie O(n))
# 2. Tworzymy n kubełków i rozrzucamy liczby z A do kubełków (jak w sortowaniu kubełkowym; złożoność O(n))
# 3. Jeśli każdy kubełek zawiera co najmniej jedną liczbę (a konkretnie---dokłandie jedną liczbę)
# to mamy dane posortowane i po prostu znajdujemy wynik w jednym liniowym przeglądzie (czas O(n))
# 4. Jeśli któryś kubełek jest pusty, to znaczy że A[i] jest minimum z któregoś kubełka a A[j] to maksimum
# z któregoś kubełka. Obliczam minimum i maksimum dla wszystkich kubełków i znajduję wynik
# przeglądając po kolei kubełki.