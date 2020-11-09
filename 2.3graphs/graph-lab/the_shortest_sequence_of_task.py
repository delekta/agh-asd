#  (najkrótszy ciąg zadań) Dany jest zbiór zadań T = {t1,...,tn}. Każde zadanie ti ma podany czas rozpoczęcia s
#  i ∈ R oraz czas zakończenia ei ∈ R. Proszę zaproponować algorytm (bez implementacji), który znajduje taki
#  podzbiór k zadań (gdzie k ∈ N to dany parametr wejściowy), że (a) żadne dwa zadania na siebie nie nachodzą
#  oraz (b) czas jaki mija od rozpoczęcia najwcześniejszego zadania do zakończenia najpózniejszego jest minimalny.
#  Jeśli podzbioru rozmiaru k spełniajacego warunki zadania nie ma, to algorytm powinien to stwierdzić. Algorytm
#  powinien być jak najszybszy. Można założyć, że żaden przedział nie jest podzbiorem innego.

"""
    Rozwiązujemy n-k razy problem wyboru zajeć O(k). Zapisujemy minimum spośrod wszystkich n - k iteracji.
    Time complexity: O((n-k)* k) ~ O(n^2)
"""