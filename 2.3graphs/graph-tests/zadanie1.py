# Królestwo Syjonu składa się z miast połączonych dwukierunkowymi drogami. Między dowolną parą miast istnieje
# jedna i tylko jedna ścieżka. Część miast została zainfekowana przez maszyny. Do eskalacji ataku dojdzie,
# jeśli znajdą się przynajmniej dwa miasta, zainfekowane przez maszyny, między którymi będzie istniała ścieżka.
# Dlatego Mofreusz postanowił zniszczyć część dróg między miastami, tak aby żadne zainfekowane miasta nie
# były połączone. Niemniej jednak każda droga ma przypisany czas potrzebny na zniszczenie. Pomóż Morefuszowi tak
# dobrać niszczone drogi, aby nie instniała ścieżka między dowolnymi zainfekowanymi miastami i czas potrzebny na
# niszczenie był minimalny. Niszczymy jedną  drogę na raz.
# Rozwiązanie:
#   Jesli chcemy wybrać krawędzie o najmniejszym czasie które chcemy zniszczyć to możemy rownież zbudować graf
#   o największy możliwych krawędziach zawierających co najwyżej jedno miasto zainfekowane, mozemy to zrobić za pomocą
#   struktury find/union. Między każdą para miast istnieje jedynie jedna ścieżka -> graf jest drzewem
# Time complexity: O(nlogn + nlog*n) log*n -> logarytm iterowany

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
        self.infected = False


def infect(x):
    x.infected = True


def make_set(i):
    return Node(i)


def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    a = find(x)
    b = find(y)

    if not (a.infected and b.infected):
        if a.rank > b.rank:
            b.parent = a
            a.infected = a.infected or b.infected
        else:
            a.parent = b
            b.infected = a.infected or b.infected
            if a.rank == b.rank:
                b.rank += 1
        return True
    else:
        return False


def destroys_paths(cities, roads):
    # sort decreasing
    roads.sort(key=lambda x: x[2], reverse=True)
    destroying_time = 0
    for road in roads:
        x = cities[road[0]]
        y = cities[road[1]]
        if not union(x, y):
            print(road)
            destroying_time += road[2]
    return destroying_time


num = 15
cities = [Node(i) for i in range(num)]
infect(cities[2])
infect(cities[4])
infect(cities[7])
infect(cities[12])
infect(cities[14])

# represented as tuple (vertex1, vertex2, value)
# Edges are undirected!!!
roads = [(0, 1, 1), (0, 2, 10), (1, 3, 7), (1, 4, 6), (2, 5, 6), (2, 6, 4), (3, 7, 5), (3, 8, 4),
         (4, 9, 3), (4, 10, 10), (5, 11, 4), (5, 12, 2), (6, 13, 2), (6, 14, 3)]

print(destroys_paths(cities, roads))
