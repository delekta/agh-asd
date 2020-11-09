# Dana jest tablica A o rozmiarze n, zawierająca liczby ze zbioru {0, ..., n^2-1}.
# Proszę podać algorytm sortujący tę tablicę w czasie O(n).

"""
Stosujemy sortowanie pozycyjne (radix sort), ale podstawą naszego systemu liczenia nie jest 10, tylko n.
 W związku z tym musimy wykonać dwa sortowania z użyciem sortowania przez zliczanie (counting sort),
 które wykona się w czasie O(n). Najpierw reszta z dzielenia przez n, pozniej dzielenie calkowitoliczbowe przez n!

"""