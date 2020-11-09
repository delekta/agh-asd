# Dane są trzy zbiory: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c z odpowiednio
# A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników! 

# Sortujemy A i B, i dla każdego elementu C, przeprowadzamy szukanie idąc dwoma wskaźnikami: jednym z początku A,
# drugim z końca B. w zależności od tego, czy suma elementów wskazywanych przez wskaźniki w A i B jest większa
# lub mniejsza niż element z C, to przesuwamy odpowiedni wskaźnik. Jak natrafimy na równą sumę,
# to raportujemy o sukcesie.
# Inne podejście polega na posortowaniu C i dla każdej pary z A i B szukamy sumy binarnie.
# Złożoności: dla wielkości tablic odpowiednio a, b i c:
# pierwsze podejście: O(alog(a) + blog(b) + c(a+b))
# drugie podejście: O(clog(c) + a*b*log(c)) = O(log(c) * (a*b + c))
