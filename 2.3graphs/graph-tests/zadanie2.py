# Dane jest n zmiennych x1, …, xn, o nieznanych wartościach. Mamy jednak podaną serię równości i różności,
# postaci: xi=xj, xi!=xj. Podaj jak najszybszy algorytm, który sprawdzi, czy podana tak seria nie jest sprzeczna.

"""
    Używamy struktury find/union
        1.Podczas pierwszej iteracji przechodzimy po rownosciach i łączymy te zmienne które są sobie rowne(za pomocą
        funkcji union)
        2. Podczas drugiej iteracji przechodzimy po nierownosciach i jesli dwie zmienne nalezały do jendnego
        zbioru(union) to zwracamy False, jesli uda nam się sprawdzić wszystkie nierówności zwracamy True
        Time complexity: (n + m) * log*k
         n -> liczba równosci
         m -> liczba nierownosci
         k -> liczba zmiennych
"""