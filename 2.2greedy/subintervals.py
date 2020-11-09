#  Dany jest zbiór przedziałów I ={[a1,b1],...,[an,bn]}.Mówimy,że przedział [ai,bi] deaktywuje przedział[aj,bj] jeśli
#  ai >= aj oraz bi <= bj (czyli pierwszy jest pod zbiorem drugiego).Proszę zaproponować algorytm, który znajduje
#  podzbiór I o maksymalnym rozmiarze taki, że żaden przedział nie jest deaktywowany przez inny (innymi słowy, należy
#  dany przedział usunąć jeśli jest nadzbiorem innego, a spośród identycznych przedziałów usunąć wszystkie poza jednym).
# Time complexity: O(n*logn)


def subintervals(intervals):
    # starts[i][2] -> flag , if flag = 0 interval is no longer considered
    starts = [[intervals[i][0], intervals[i][1], 1] for i in range(len(intervals))]
    starts.sort(key=lambda x: x[0])
    ends = [[starts[i][1], i] for i in range(len(intervals))]
    ends.sort(key=lambda x: x[0])
    print(starts)
    print(ends)

    s = 0
    e = 0
    res = []

    while s < len(starts) and e < len(ends):
        end = ends[e]
        # print(s, e)
        if starts[end[1]][2] == 1:
            # print(end[1])ee
            if end[1] == s:
                # print(end[1])
                while s + 1 < len(starts) and e < len(ends) and starts[s + 1][1] == end[0]:
                    starts[s][2] = 0
                    e += 1
                    s += 1
                # print(s)
                res.append(starts[s])
                # needed
                e += 1
            else:
                starts[s][2] = 0
        else:
            e += 1  # if starts[end[1]][2] == 0 we want move only e
        if starts[end[1]][2] != 0:
            s += 1
    return res


# array represented as (range_start, range_end)
intervals = [(0, 2), (1, 2), (2, 3), (5, 9), (5, 7), (7, 8), (8, 10)]
intervals2 = [(0, 10), (1, 9), (2, 7), (2, 5), (3, 5), (4, 4)]
print(subintervals(intervals))