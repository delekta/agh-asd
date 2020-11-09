# Pewien eksperyment fizyczny generuje bardzo szybko stosunkowo krótkie ciągi liczb całkowitych z przedziału
# od 0 do 10^9-1. Pomiar w eksperymencie polega na okresleniu ile różnych liczb znajduje się w danym ciągu.
# Niestety liczby są generowane tak szybko, że konieczne jest zagwarantowanie czasu działania rzęduO(1)
# na każdy element ciągu (pamięć jest dużo mniej krytycznym zasobem). Ciągi są generowane błyskawicznie,
# jeden po drugim. Proszę zaproponować strukturę danych pozwalającą na wykonywanie następujących operacji:
# TRUDNE

"""
 init() - przygotowuje strukturę danych do pracy • insert(x) - wstawia x do struktury; zwrace True,
 jeśli x nie była jeszcze wstawiona i False w przeciwnym razie • reset() - usuwa wszystkie liczby

Wszystkie operacje powinny działać w czasie O(1) (pomijając koszt alokacji pamięci w funkcji init()).

Rozwiązanie: Tworzymy dwie tablice:
• A – tablica (indeksowana od 0 do 10^9-1). Każde pole A[i] ma dwa pola: A[i].reported (informacja czy
liczba i się pojawiła) oraz A[i].ptr (wskaźnik)
• S – tablica o rozmiarze równym maksymalnej długości ciągu w eksperymencie, używana jako stos na wskaźniki

init(): alokuje te dwie tablice i zapisuje, że stos S jest pusty. Wymaga to czasu O(1)
(nie licząc systemowego czasu na alokację pamięci)

reset(): zapisuje, że stos S jest pusty (czas O(1))

insert(x): Idea jest taka, że początkowo A[x].reported powinno mieć wartość False. Widząc to,
wpisalibyśmy A[x].reported = True i zwrócili False. Gdyby A[x].reported = True, to zwrócilibyśmy False.
Ale to nie do końca działą, bo nie możemy wyzerować tablicy A. Dlatego stosujemy strategię, w której możemy
zweryfikować, czy A[x].reported ma poprawną wartość.
1. Sprawdzamy, czy A[x].ptr wskazuje na obszar tablicy S, w której przechowywane są elementy stosu.
Jeśli nie, to wpisujemy do A[x].reported wartość False (bo nie widzieliśmy jeszcze wcześniej liczby x).
Następnie umieszczamy na stosie S wskaźnik na A[x], a A[x].ptr wskaźnik do tego właśnie dodanego elementu stosu.

2. Jeśli A[x].ptr wskazuje na obszar stosu, to sprawdzamy czy znajdujący się tam wskaźnik z powrotem wskazuje na A[x].
 Jeśli tak, to A[x].reported ma poprawną wartość. Jak nie, to wpisujemy do A[x].reported wartość False i postępujemy
 jak wyżej (dodajemy odpowiedni wskaźnik na stos i w A[x[.ptr umieszczamy wsaźnik zwrotny) 3. Po wykonaniu powyższych,
 wiemy że A[x].reported ma poprawną wartość.
Rozwiązanie opiera się na tym, że w obszarze stosu zawsze mamy poprawne wartości. Tak więc element A[x]
musi „udowodnić”, że ma poprawną wartość przez wskazanie „o ten element na stosie mówi, że jestem poprawny”.
Jeśli element na stosie faktycznie to mówi (jest tam wskaźnik zwrotny) to element A[x] poprawny jest. A jak nie, to nie.
"""