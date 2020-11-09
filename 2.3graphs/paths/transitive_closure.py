# Domknięciem przechodnim skierowanego grafu G = (V,E) nazywamy taki graf G0 = (V,E0), że dla każdych dwóch
# wierzchołków u,v ∈ V graf G0 ma krawędź z u do v wtedy i tylko wtedy, gdy w G jest skierowana ścieżkaz u do v.
# Proszę zaimplementować funkcję tclosure( G ),która na wejście otrzymuje graf skierowany w reprezentacji macierzowej
# (bez wag; G[i][j] to wartość logiczna mówiąca czy istnieje krawędź z i do j) i zwraca graf będący domknięciem
# przechodnim G (w tej samej reprezentacji).
# def tclosure( G ): # policz domknięcie przechodnie G i je zwróc
# G = [
# [False, True , False],
# [False, False, True ],
# [False, False, False]
# ]
# print( tclosure( G ) )
# wypisze #
# [[False, True , True],
# [False, False, True],
# [False, False, False]]


def transitive_closure(graph):

    reach = [i[:] for i in graph]
    print_matrix(reach)
    for k in range(len(graph)):

        for i in range(len(graph)):

            for j in range(len(graph)):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print("\n")


G = [
    [False, True, False],
    [False, False, True],
    [False, True, False]
]
print_matrix(transitive_closure(G))