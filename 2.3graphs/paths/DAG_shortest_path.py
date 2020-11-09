#  Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w
#  acyklicznym graﬁe skierowanym? (Krawędzie są ważone.)
# Topological sort time complexity: O(V + E)
"""
    1. Topological Sort na Grafie
    2. Jak mamy posortowane topologicznie, to wystarczy raz przejsc po krawędziach bellman-fordem, bo relaksujemy
        tylko wierzcholki ktore sa przed nami, wiec gdy wchodzimy w wierzcholek to mamy pewnosc ze on juz jest
        maksymalnie zrelaksowany
"""
