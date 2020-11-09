# Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem danego
# języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać spacje
# do wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa” możemy
# zapisać jako “ala ma kota i nie ma psa”. Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe poprawne
# rodzielenie stringa spacjami, jeśli oczywiście ono istnieje. Algorytm ma być szybki, ale najważniejsze,
# żeby był poprawny!!!. -> podpowiedz: raczej nie będzie to liniowe ani nlogn.
# Time complexity: O(n^2) can be O(n *s) s -> length of the longest word

# i assume that it works O(1)
def check(str):
    dictionary = ["ala", "ma", "kot", "kota", "i", "nie", "psa"]
    for word in dictionary:
        if str == word:
            return True
    return False


def correct_words(str):
    dp = [False for _ in range(len(str) + 1)]
    dp[0] = True
    for i in range(len(str) + 1):
        for j in range(i, -1, -1):
            if check(str[j:i]):
                dp[i] = dp[j]
            if dp[i]:
                break
    print(dp)
    return dp[len(str)]


str = "alamakotainiemapsa"
print(correct_words(str))