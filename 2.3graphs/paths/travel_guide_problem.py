# Przewodnik chce przewieźć grupę turystów z miasta A do miasta B. Po drodze jest jednak wiele innych miast i
# między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci (x,y,c), gdzie
# x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów. Proszę zaproponować algorytm,
# który znajduje trasę z A do B, po której może przejechać możliwie jak największa grupa turystów bez rozdzielania się.

"""
    1. Dijkstra, tylko szukamy sciezki maksymalnej, z kolejki ściagamy wierzchołek o najwiekszej wagowo krawędzi
        i warunek v.d < min(u.d, weight[u][v]
    2. Interesuje nas ścieżka z najwiekszą przpustowością, czyli de facto najwiekszej krawedzi minimalnej
"""