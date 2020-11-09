# Proszę zaimplementować klasę IntervalSums, która przechowuje tablicę n liczb (na pozycjach od 0 do n−1),
# pozwala zmieniać zadane liczby oraz obliczać sumę liczb na pozycjach od i do j.
# Państwa kod będzie uruchamiany. Proszę zaimplementować następujące funckcje w klase
# IntervalSums (można też dopisać inne klasy i/lub funkcje):
# class IntervalSums:
#   def __init__(self, n):
#       tworzy tablcę rozmiaru n, zainicjowaną zerami
#   def set( self, i, val ):
#       zmienia zawartosc tablicy pod indeksem i na val
#   def interval( self, i, j ):
#       zwraca sumę elementów tablice na pozycjach od i do j wlacznie


class IntervalSums:
    def __init__(self, n):
        self.len_array = n
        self.len_tree = self.set_len(n)
        self.tree = [0 for _ in range(2 * self.len_tree)]

    def set_len(self, length):
        l = 1
        while l < length:
            l *= 2
        return l

    def set(self, i, val):
        self.set_i_to_val(0, self.len_array - 1, i, val, 0)

    def set_i_to_val(self, start, end, i, val, curr):
        if start == end == i:
            self.tree[curr] = val
            return self.tree[curr]
        mid = start + (end - start) // 2
        if i <= mid:
            self.tree[curr] = self.set_i_to_val(start, mid, i, val, 2 * curr + 1) + self.tree[2 * curr + 2]
            return self.tree[curr]

        else:
            self.tree[curr] = self.set_i_to_val(mid + 1, end, i, val, 2 * curr + 2) + self.tree[2 * curr + 1]
            return self.tree[curr]

    def interval(self, i, j):
        return self.sum_from_i_to_j(0, self.len_array - 1, 0, i, j)

    def sum_from_i_to_j(self, start, end, curr, i, j):
        if i == start and j == end:
            return self.tree[curr]
        # poprawka
        # elif j < start or end < i:
        #     return 0
        mid = (start + (end - start) // 2)
        if i <= mid < j:
                                                        # wazne rozdzielenie szukanych przedziałow
            return self.sum_from_i_to_j(start, mid, 2 * curr + 1, i, mid) + \
                    self.sum_from_i_to_j(mid + 1, end, 2 * curr + 2, mid + 1, j)
        elif i <= j <= mid:
            return self.sum_from_i_to_j(start, mid, 2 * curr + 1, i, j)
        elif mid < i <= j:
            return self.sum_from_i_to_j(mid + 1, end, 2 * curr + 2, i, j)

    def check(self):
        while True:
            print(" s - set(i, val) \n i - interval(i, j) \n e - (end)")
            opr = input("Podaj komende:")
            if opr == 's':
                i = int(input("Podaj indeks:"))
                val = int(input("Podaj wartosc: "))
                self.set(i, val)
                print(self.tree)
            elif opr == 'i':
                i = int(input("Podaj i:"))
                j = int(input("Podaj j:"))
                sum = self.interval(i, j)
                print(sum)
            elif opr == 'e':
                break
            else:
                print("Komenda ", opr, " nie istnieje")


Sum = IntervalSums(6)
Sum.check()

