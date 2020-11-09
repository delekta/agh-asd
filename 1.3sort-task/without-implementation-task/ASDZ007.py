# Proszę zaproponować algorytm, który na wejście dostaje tablicę A słów (być może o różnych długościach)
# i sortuje je w porządku słownikowym w czasio O(L), gdzie L to suma długości słów.

"""
Rozwiązanie: Najpierw sortujemy wyrazy po długości (przez zliczanie). Następnie sortujemy wyrazy pozycyjnie
z tą poprawką, że dla każdej pozycji 'i' znamy 'k' takie, że tab[:k] zawiera wyrazy krótsze od 'i'.
I na pozycji 'i' sortujemy jedynie fragment tab[k:]. Gdy wyrazy są posortowane po długościach, to
indeksy 'i' możemy wyznaczyć w czasie O(długość najdłuższego słowa). Całość działa, bo w sortowaniu
pozycyjnym używamy sortowania stabilnego.

"""