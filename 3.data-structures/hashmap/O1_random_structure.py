# Zaprojektuj strukturę danych przechowującą liczby naturalne, udostępniającą następujący Interfejs:
# insert(num) - umieszcza w strukturze liczbę naturalną.
# delete(num) - usuwa ze struktury liczbę
# find(num) - sprawdza czy liczba jest w strukturze.
# getRandom() - zwraca losową liczbę ze struktury. Do tej funkcji możesz wykorzystać funkcję randInt(N), która
# w czasie O(1) zwraca losową liczbę naturalną z zakresu od 0 do N-1.
# Wszystkie powyższe funkcje powinny działać w czasie O(1) zawsze!!!.

# Rozwiązanie: Mając randInt(N) można łatwo losować liczbę z tablicy, ponieważ wystarczy wylosować indeks
# poprzez randInt(len(array)). Dlatego w rozwiązaniu łączymy słownik ze zwykłą tablicą. Kluczami w słowniku
# będą przechowywane liczby. Dodatkowo liczby te będziemy przechowywać w tablicy i indeks po jakim się
# znajdują w tablicy będzie wartością pod odpowiednim kluczem w słowniku.

# insert(num) - wstawiamy element na koniec tablicy, a potem do słownika. Pod kluczem num umieszczamy
# wartość len(array)-1
# find(num) - tak jak wyszukiwanie w słowniku
# delete(num) - znajdujemy pod jakim indeksem w tablicy znajduje się num i umieszczamy tam wartość
# ostatniego elementu tablicy, potem podmieniamy w słowniku indeks pod, którym znajduje się ostatni element
# w tablicy. Na końcu usuwamy ostatni element tablicy. (jest to O(1), tylko usuwanie ze środka daje O(n)).
# getRandom() - losujamy indeks z tablicy.
from random import randint


class RandomHashSet:
    def __init__(self):
        self.array = []
        self.dict = {}

    def insert(self, num):
        self.array.append(num)
        self.dict[num] = len(self.array) - 1

    def find(self, num):
        return num in self.dict

    def get_random(self):
        return self.array[randint(0, len(self.array) - 1)]

    def delete(self, num):
        index = self.dict[num]
        last = self.array[len(self.array) - 1]
        self.array[index] = last
        self.dict[last] = index
        del self.dict[num]
        self.array.pop()


s = RandomHashSet()

s.insert(12)
s.insert(22)
s.insert(32)
s.insert(42)
s.insert(52)

print(s.get_random())

s.delete(32)

print(s.array)
