# Sortowania liniowe
# Zadanie 4
# Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb
# naturalnych długości n o zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) -
# ma ona zwracać informację o tym, ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
# Można założyć, że zawsze a >= 1, b <= k.
# Pomysl: uzyjemy cumulative sum z Counting Sorta


class Database:
    def __init__(self, arr):
        k = max(arr) + 1
        self.C = [0] * k
        for i in range(len(arr)):
            self.C[arr[i]] += 1
        for i in range(1, k):
            self.C[i] += self.C[i - 1]

    def count_num_in_range(self, a, b):
        return self.C[b] - self.C[a - 1]


arr = [5, 3, 2, 1, 8, 9, 2, 2, 1, 24, 21, 21, 15, 14]
ob = Database(arr)
print(ob.count_num_in_range(2, 7))
