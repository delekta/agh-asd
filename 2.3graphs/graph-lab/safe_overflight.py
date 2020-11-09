# Zadanie 7. (bezpieczny przelot) Dany jest graf G = (V,E), którego wierzchołki reprezentują punkty nawigacyjne
# nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy korytarz powietrzny
# ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈N (wyrażonym w metrach). Przepisy dopuszczają przelot
# danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t metrów. Proszę zaproponować algorytm
# (bez implementacji), który sprawdza czy istnieje możliwość przelotu z zadanego punktu x ∈ V do zadanego punktu
# y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu. Algorytm powinien być poprawny i możliwie jak
# najszybszy. Proszę oszacować jego złożoność czasową.


def DFS(s, t, graph, flight_ceiling, d, visited, parents):
    if s == t:
        return True
    visited[s] = True
    for i in range(len(graph[s])):
        # In adjacency list remember that to call value you must use different indices than when you want save parents
        v = graph[s][i][0]
        if not visited[v]:
            if flight_ceiling - d <= graph[s][i][1] <= flight_ceiling + d:
                parents[v] = s  # !!!
                if DFS(graph[s][i][0], t, graph, flight_ceiling, d, visited, parents):
                    return True
    return False


def print_path(s, t, parents):
    if t == s:
        print(t, end=" ")
        return
    print_path(s, parents[t], parents)
    print(t, end=" ")


# edge (destination vertex, height)
graph = [
    [(1, 970), (7, 1400)],
    [(0, 970), (2, 1200), (7, 1000)],
    [(1, 1200), (3, 500), (5, 700), (8, 880)],
    [(2, 500), (4, 1025), (5, 1050)],
    [(3, 1025), (5, 500)],
    [(3, 1050), (4, 500), (6, 995)],
    [(5, 995), (7, 1300), (8, 1100)],
    [(0, 1400), (1, 1000), (6, 1300), (8, 980)],
    [(2, 880), (6, 1100), (7, 1300)],
]


visited = [False for _ in range(len(graph))]
parents = [-1 for _ in range(len(graph))]
s = 0
t = 4
flight_ceiling = 1000
d = 100

if DFS(s, t, graph, flight_ceiling, d, visited, parents):
    print_path(s, t, parents)
else:
    print("The path from", s, "to", t, "doesnt exist!")
