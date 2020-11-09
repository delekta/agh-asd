# Dana jest tablica zawierająca liczby całkowite (również ujemne). Należy przeprowadzić
# preprocessing, tak by móc być w stanie odpowiadać na następujące zapytania w czasie                          
# O(log(n)):  Zapytanie to liczba całkowita x. Podczas odpowiedzi na jedno zapytanie, należy: 
# 1. “wirtualnie” dodać x do każdego elementu w tablicy 
# 2. zwrócić sumę wartości bezwzględnych wszystkich elementów tablicy. 
# Uwaga! Dodane “wirtualnie” wartości x akumulują się na kolejne zapytania, tzn. po
# wykonaniu zapytania dla x=2 “wirtualnie” dodano wszędzie 2, a dla kolejnego zapytania                        
# x=3 “wirtualnie” trzeba dodać wszędzie 3, a liczby będą łącznie “wirtualnie” większe o 5                            
# względem tego, co faktycznie jest w tablicy. 

# P - tablica sum prefiksowych
# S - tablica sum suffiksowych

# Sortujemy tablicę. Wyznaczamy tablicę sum prefixowych i suffixowych. Każde zapytanie, to wyszukanie binarnie,
# gdzie w tablicy zaczynają się elementy, takie, że nawet po dodaniu sumy wszystkich dotychczasowych x z zapytań,
# będą liczby ujemne. Wyznaczamy binary searchem elementy ktore nawet po dodaniu ujemne czyli szukamy -curr_x
# Gdzie curr_x += x, bo dla curr_x = 5 szykamy gdzie w tablicy wystepuje -5 bo wiemy ze to po dodaniu bedzie juz dodatnie
# wtedy zwracamy abs( P[idx - 1] + curr_x * idx) + S[idx] + curr_x * (n - idx), gdzie n to dlugosc tablicy
