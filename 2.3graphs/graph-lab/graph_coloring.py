# Zadanie 1. (kolorowanie grafu) Mamy dany nieskierowany graf G = (V,E). Dla każdego wierzchołka v należy
# wybrać liczbę naturalną f(v) (nazywaną kolorem v) tak, żeby dla każdej krawędzi{x,y}∈ E zachodzilo, ze f(x) != f(y).
# Należy użyć jak najmniej kolorów (czyli zbior f(V ) powinien mieć minimalną liczność). Problem jest NP-zupełny więc
# nie istnieje optymalny algorytm wielomianowy (o ile P jest różne od NP). Proszę podać algorytm zachłanny, który używa
# najwyżej D+1 kolorów, gdzie D to maksymalny stopień wierzchołka w G.

"""
    Sposob optymalny:
        Zadanie kolorowania wierzchołków grafu najmniejszą możliwą liczbą kolorów da się rozwiązać za pomocą algorytmu,
    który sprawdza kolejno wszystkie możliwe układy kolorów wierzchołków i wybiera ten układ, w którym zużyta jest
    najmniejsza liczba kolorów. Podstawowym problemem jest tutaj tworzenie kombinacji kolorów poszczególnych
    wierzchołków. Na szczęście problem ten rozwiązujemy prosto metodą licznika. Wyobraźmy sobie, że poszczególne
     wierzchołki grafu są kolejnymi cyframi licznika. Na początku przyjmujemy podstawę 2. Złozoność czasowa O((2^n)*n)
     Algorytm zachłanny:
        Nie gwarantuje uzycia minimalnej liczby kolorow, ale nigdy nie uzyje wiecej niz d + 1 kolorow, gdzie d to najwiekszy
    stopien wsrod wierzcholkow w grafie. Złozoność czasowa O(V^2 + E)
"""