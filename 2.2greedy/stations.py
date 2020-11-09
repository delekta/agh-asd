# (problem stacji benzynowych) Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód
# spala dokładnie jeden litr paliwa na jeden kilometr trasy (można powiedzieć, że jedzie czołgiem... znaczenie
# punktów A i B w ramach obecnej sytuacji geopolitycznej wybierzcie sobie sami). W baku mieści się dokładnie D
# litrów paliwa. Trasa z A do B to prosta, na której znajdują się stacje benzynowe.
# Mamy dwa różne zadania (rozwiązywane osobno):
#  -> wyznaczyć trasę, na której tankujemy minimalną liczbę razy
#  -> wyznaczyć trasę, której koszt jest minimalny (wówczas znamy jeszcze dla
#     każdej stacji cenę za litr paliwa, nie musimy zawsze tankować do pełna).
#  -> ale jeśli na stacji tankujemy, to musimy zatankować do pełna.


"""
    1. Tankujemy na najdalszej stacji do której możemy dojechać. Tankowanie wcześniej pozbawia nas optymalnego, ale
        zmiana tankowania na dalszą, która jest dalej w zasięgu nie pozbawia nas optymalnego
    2. Dojeżdzamy do stacji i jesli z tej stacji jestesmy w stanie dojechac do innej stacji w ktorej cena za paliwo
        jest mniejsza niż ta na której stoimy, to tankujemy tylko tyle żeby dojechac do kolejnej, jesli nie ma w
        zasiegu stacji która ma ceny niższe niż nasza to tankujemy do pełna i przejezdzamy do stacji o najniższych cenach
        w zasiegu.
    3. Podpowiedz: w dynamikach zawsze zastanów się czego szukasz to bedzie w polu dp[len1 - 1][len2 - 2]
        i teraz juz wiesz jak powinna wygladac cała funkcja dynamiczna.
        f(i) - funkcja zwracajaca minimalny koszt dojechania do stacji i-tej
        c(i) - koszt tankowania na i-tej stacji
        d(i) - odległość  i-tej stacji od poczatku

        f(i) = min(f(j) + (d(i)- d(j)) * k(i)), przy założeniu że d(i)- d(j) <= D, D - pojemnosc baku

"""