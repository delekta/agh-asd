# Oswald Cobbelpot chce przejąć władzę nad Gotham. W tym celu musi zdobyć pieniądze z kryjówek ojca mafii Don Falcona.
# Kryjówki Don Falcona połączone są przejściami podziemnymi, tak, że tworzą drzewo skierowane, o korzeniu w pewnej
# kryjówce początkowej. W każdej kryjówce jest pewna ilość pieniędzy. Oswald może zabierać pieniądze z kryjówek,
# ale musi przestrzegać jednej zasady: jeżeli zabierze pieniądze z jednej kryjówki, to nie może zabrać
# z żadnej w jej poddrzewie.
# Zaproponuj algorytm, który powie Oswaldowi, ile maksymalnie pieniędzy może zdobyć. Lepiej, żeby był jak najszybszy,
# ponieważ Oswald jest nieobliczalny, gdy musi czekać…… :)
# v = max(v, sum_of_child_val) bottom up


class Vertex:
    def __init__(self, val):
        self.val = val
        self.children = []


def maximum(s, child=0):
    if not s.children:
        return s.val

    for v in s.children:
        child += maximum(v)

    return max(s.val, child)


v1 = Vertex(10)
v2 = Vertex(7)
v3 = Vertex(7)
v4 = Vertex(5)
v5 = Vertex(4)
v6 = Vertex(3)
v7 = Vertex(3)

v1.children.append(v2)
v1.children.append(v3)

v2.children.append(v4)
v2.children.append(v5)

v3.children.append(v6)
v3.children.append(v7)

print(maximum(v1))
