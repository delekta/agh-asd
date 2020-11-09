# Mamy dany graf G = (V,E) z wagami w:E →N−{0}(dodatnie liczby naturalne). Chcemy znalezc scieżkę
# z wierzchołka u do v tak, by iloczyn wag był minimalny. Proszę zaproponować algorytm.

"""
      Gdybyśmy na wierzchołkach trzymali iloczyn to narazilibysmy się na szybki "overflow"
    1. Chcemy zeby iloczyn wag krawędzi po których przejdziemy był minimalny, wiec mozemy przkształcić funkcje wagowa
        zeby nie trzymała wag, a logarytmy tych wag i szukamy minimalnej sumy, bo jesli chcemy zeby iloczyn był minimalny
        to mozemy szukac minimalnej sumy wag logarytmow, bo np jesli loga + logb + logc jest minimalna to
        log(a*b*c) jest minimalna czyli a*b*c jest minimalne
"""