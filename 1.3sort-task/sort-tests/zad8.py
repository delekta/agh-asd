# Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, w którym z nim należy
# wybudować dom, tak aby suma euklidesowych odległości od tego punktu do wszystkich pozostałych była minimalna.
# Należy zwrócić również tę sumę. Algorytm powinien być jak najszybszy. 

# Rozwiazanie O(n):
# Quickselect znalezc mediane(srodkowy punkt) jesli nieparzysta liczba elementow, jeden z srodkowych(obojetnie)
# gdy parzysta liczba elementow. Jest to poprawane rozwiazanie, (dla ulatwienia zalozmy ze mamy 2n + 1 elementow
# gdyż jesli jestemy w medianie to jakikowiek ruch zwieksza nam sume odlegosci, gdy ruszamy sie w prawo o k to
# oddalamy sie od od n + 1 elementow o k, a zblizamy sie do n elementow(czyli suma odleglosci rosnie)
# ,w druga strone ta sytuacja wygloda tak samo
