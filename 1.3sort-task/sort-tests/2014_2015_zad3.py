# Jak posortować n-elementową tablicę liczb rzeczywistych, które przyjmują tylko logn różnych wartości?
# Uzasadnić poprawność algorytmu i oszacować złożoność.

"""
    Rozwiazanie:
    1. Przepisujemy elementy do nowej tablicy jako krotki(unikalny_element, ilosc), sprawdzamy binary_search'em
        czy element nalezy do tablicy jesli tak to zwiekszamy ilosc, jesli nie to mamy juz znalezione dla niego miejsce,
        przesuwammy elementy w tablicy w prawo i wstawiamy nowy element na swoje miejsce, tym samym utrzymujemy
        posortowana tablice (przesuwanie nie jest tak istotne, poniewaz bedzie zdazalo sie stosunkowo rzadko)
    2. Przepisujemy do wynikowej
    Time complexity: n * log(logn)

"""