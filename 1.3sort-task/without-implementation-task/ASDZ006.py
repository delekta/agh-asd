#  Proszę zaproponować algorytm, który mając na wejściu dwa słowa, x i y, składające się z małych liter
#  alfabetu łacińskiego sprawdzi, czy słowa te są anagramami (czyli zawierają tyle samo, tych samych liter).

"""
Rozwiązanie: Najpierw sprawdzamy czy słowa są jednakowej długości (jak nie, to słowa nie są anagramami).
Tworzymy tablicę liczników L o rozmiarze alfabetu (nie musimy całej tablicy zerować)
Przebiegamy po słowie x zerując liczniki dla liter w słowie x - O(N)
Przebiegamy po słowie y zerując liczniki dla liter w słowie y - O(N)
Przebiegamy po słowie x zwiększając o jeden  liczniki dla liter w słowie x - O(N)
Przebiegamy po słowie y zmniejszając o jeden  liczniki dla liter w słowie y - O(N)
Przebiegamy po słowie x sprawdzając czy liczniki dla liter w słowie x są równe zero - O(N)
Przebiegamy po słowie y sprawdzając czy liczniki dla liter w słowie y są równe zero - O(N)
Jeżeli wszystkie liczniki dla liter x i y są równe zero słowa są anagramami

"""