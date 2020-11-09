#  Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
#  Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym rozkładem)
#  n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo ceil(logn) elementów powstałej
#  tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę zaproponować (bez implementacji!)
#  algorytm sortowania tak powstałych danych. Algorytm powinien być możliwie jak najszybszy.
#  Proszę oszacować i podać jego złożoność czasową.
# In computer science all logarithms presumed to be base-2

"""
 1. Przepisac liczby parzyste do nowej tablicy.
 2. Posortowac tablice z liczbami parzystymi O(logn * log(logn)).
 3. Scalic dwie tablice, przepisujac do wynikowej zawsze element mniejszy.
    (Z pierwszej tablicy przepisujemy tylko liczby nieparzyste) O(n)
"""