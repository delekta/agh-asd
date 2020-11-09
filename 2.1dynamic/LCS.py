# Longest common subsequence


# top-down recursive O(2^n)
def lcs_r(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        return 1 + lcs_r(str1, str2, i + 1, j + 1)
    else:
        return max(lcs_r(str1, str2, i + 1, j), lcs_r(str1, str2, i, j + 1))


# bottom-up O(len(str1) x len(str2))
# word in table start from 1 beacause we must have sth to start
# index 0 is reserved for initial value 0
def lcs(str1, str2):
    LCS = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        LCS[i][0] = 0
    for i in range(len(str2) + 1):
        LCS[0][i] = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                LCS[i][j] = 1 + LCS[i - 1][j - 1]
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    res = LCS[len(str1)][len(str2)]
    s1 = len(str1)
    s2 = len(str2)
    ans = []
    while s1 != 0 and s2 != 0:
        if LCS[s1][s2] - 1 == LCS[s1 - 1][s2 - 1]:
            # Tablica LCS jest przesunieta, wiec musimy tez przesunac indeksy od str1
            ans.append(str1[s1 - 1])
            s1 -= 1
            s2 -= 1
        elif LCS[s1][s2] == LCS[s1][s2 - 1]:
            s2 -= 1
        else:
            s1 -= 1

    print(res, ans)


str1 = "abd"
str2 = "asdfbaa"
print(lcs_r(str1, str2, 0, 0))
print(lcs(str1, str2))
