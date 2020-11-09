# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n.
# Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.
#
# Solution 1: O(mlogm + nlogn)
#   1. Sort first and second array
#   2. Use merge as process to compare elements
#
# Solution 2(better one): O(mlogm + nlogm), because m << n
#   1. Sort first array(smaller one)
#   2. Iterate through every element of second array and use binary search to search every element in first array
