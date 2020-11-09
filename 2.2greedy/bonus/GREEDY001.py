# Zadanie 6
# Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm, który usunie ze
# stringa duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.
# Przykład: cbacdcbc, odpowiedzią jest acdb.


def the_least(str):
    count = [0] * 26
    visited = [False] * 26
    res = []

    for letter in str:
        count[ord(letter) - ord('a')] += 1

    for letter in str:
        count[ord(letter) - ord('a')] -= 1

        if not visited[ord(letter) - ord('a')]:

            if len(res) > 0 and count[ord(res[-1]) - ord('a')] > 0 and letter < res[-1]:
                visited[ord(res[-1]) - ord('a')] = False
                res.pop()

            res.append(letter)
            visited[ord(letter) - ord('a')] = True

    print(res)


str = 'cbacdcbc'
the_least(str)
