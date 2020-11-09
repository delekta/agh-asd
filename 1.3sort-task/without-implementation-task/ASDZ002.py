# ( Problem pojemnikow z woda) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów (2d), rury nie maja objętości (powierzchni). Każdy pojemnik opisany
# jest przez współrzędne lewego górnego rogu i prawego dolnego rogu. Wiemy, że do pojemników nalano wody
# (oczywiście woda rurami spłynęła do najniższych pojemników). Proszę podać algorytm Obliczający
# ile pojemników zostało w pełni zalanych

"""
Stwórzmy strukture która umożliwi nam efektywne działanie na pojemnikach. Kazdy pojemnik bedziemy reprezentować
jako 2 punkty, a kazdy punkt jako liste 3 elementow [y, szerekosc, flaga], gdzie y to wspolrzedna y, szerekosc
to szerekosc pojemnika, a flaga to informacja czy to jego dolny, czy gorny punkt. Strukture nastepnie
sortujemy wzgledem y, i przezchodzimy cala tablice wykonujac nastepujace operacje: pamietamy ogolna
szerekosc pojemnikow,
- jesli punkt jest poczatkiem pojemnika, obliczamy ilosc wody, i zwiekszamy szerokosc
- jesli punkt jest koncem pojemnika, obliczamy ilosc wody, i zmiejszamy szerokosc ilosc wody to szerekosc * wysokosc,
gdzie wysokosc to roznica miedzy y i-tego ora (i - 1) elementu   za kazdym razem ilosc wody odejmujemy
od calkowitej wartosci, a gdy jestemy w punkcie konca i calkowita ilosc wody jest nieujemna zwiekszamy licznik pojemnikow

zlozonosc O(nlogn) lub O(n) w zaleznosci od sortowania

Dopowiedzenie: brakuje rozwiązania kwestii, gdzie może istnieć kilka takich samych pojemników
(np gdyby to była siatka wyglądająca jak Manhattan) -> mozna zamiast if' a zrobic while ze bierzemy punkty dopoki maja
ta samo flage i te sama wysokosc i pozniej obliczamy

Istnieje także rozwiązanie, które nie wykorzystuje sortowania (ale używa wyszukiwania binarnego)
"""