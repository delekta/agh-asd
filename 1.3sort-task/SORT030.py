# Zadanie 9
# Dane jest słowo będące tablicą n znaków z alfabetu E, o rozmiarze |E|. Dana jest również liczba k.
# Długość słowa wynosi co najmniej |E|^k. Zaproponuj algorytm, który zwróci najczęściej powtarzający
# się w tym słowie podciąg o długości k. Algorytm ma działać w czasie O(n),wykorzystywać O(1) pamięci.
# Ponadto zawartość tablicy po wykonaniu algorytmu powinna pozostać niezmieniona.
# Hint: zadanie jest trudne :).

# Pomysl: Należy potraktować litery alfabetu, jako cyfry systemu liczbowego. Wtedy podciągi o długości k będą liczbami z zakresu od
# 0 do E^K-1. możemy zatem E^K początkowych pozycji naszego słowa wykorzystać do przechowywania liczników liczb odpowiadających odpowienim indeksom. Zeby nie niszczyć naszego słowa to po indeksem i przechowujemy K*(licznik wystąpień liczby i ) + wartość litery
# w początkowym słowie pod indeksem i. Wtedy możemy po zakończeniu operacji przywrócić początkową zawartość słowa poprzez operację
# %.