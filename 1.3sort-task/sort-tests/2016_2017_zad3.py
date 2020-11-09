# Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien ciąg n liter
# oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów mogących stanowić
# rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że ciąg składa się wyłącznie z liter a i b.
# Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który powtarza się dwa razy
# (to, że te wystąpienia na siebie nachodzą nie jest istotne).
# Zaproponowany algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.

"""
Z użyciem słowników:
 1. Przepisujesz wszystkie wyrazy dlugosci do słownika, jesli jeszcze go nie ma to tworzysz nowy klucz,
    jesli jest to inkremetujesz jego value O(n)
 2. na koncu przechodzisz po slowniku i szukasz maxa O(n)

Lepsze rozwiazanie:
 1. Liniowo wycinamy wszystkie spojne podciagi o dlugosci k i wkladamy do jakiejs tablicy
 2. Radix sort na tej tablicy
 3. Pozniej przechodzimy po tej tablicy i jesli poprzedni element jest taki sam jak aktualny to zwieksz licznik,
    jesli licznik wiekszy od max_length to max_length podstaw licznik i string podstaw aktualny

    Mozna tez zamienić na binarna, tak że a -> 1, b -> 0 i np aba -> 101 i zrobic tablcie count gdzie
    inkrementowalibysmy po indexie(wartosc ciagu aba po zamianie na dziesietny)
    ale przy dlugich ciagach ten sposob staje sie niewydajny
"""


