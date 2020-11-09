# Zadanie 3
# Proszę zaimplementować rozwiązanie problemu “Impraza firmowa” tak, by zwra-
# cane były imiona pracowników, którzy idą na imprezę. Należy założyć, że pra-
# cownicy reprezentowani są w strukturze:
# class Employee:
# def __init__(self, fun, name):
#   self.emp  = []
#   self.fun  = fun
#   self.name = name
# wolno dokładać własne pola do struktur


class Employee:
    def __init__(self, name, fun):
        self.emp = []
        self.fun = fun
        self.name = name
        self.f = -1
        self.g = -1


# wartosc najlepszej imprzey w poddrzewiu v, v idzie na impreze
def f(v):
    if v.f >= 0:
        return v.f

    x = v.fun
    for vi in v.emp:
        x += g(vi)

    y = g(v)
    v.f = max(x, y)

    return v.f


# wartosc najlepszej imprezy w poddrzewiu v, v nie idzie na impreze
def g(v):
    if v.g >= 0:
        return v.g
    # wazna linijka
    v.g = 0
    for vi in v.emp:
        v.g += f(vi)

    return v.g


def get_name(v, names, a):
    if a:
        if v.f > v.g:
            names.append(v.name)
            for vi in v.emp:
                get_name(vi, names, 0)
        else:
            for vi in v.emp:
                get_name(vi, names, 1)
    else:
        for vi in v.emp:
            get_name(vi, names, 1)



Jan = Employee("Janek", 5)
for i in range(2):
    name = str(input("Podaj imie pracownika:"))
    fun = int(input("Podaj fun: "))
    Jan.emp.append(Employee(name, fun))
    for j in range(2):
        name2 = str(input("Podaj imie pracownika:"))
        fun = int(input("Podaj fun: "))
        Jan.emp[i].emp.append(Employee(name2, fun))

names = []
fun = f(Jan)
print(fun)
get_name(Jan, names, 1)
print(names)




