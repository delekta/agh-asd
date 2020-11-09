# gra jaka to liczba
print("Witaj w grze jaka to liczba.")
print("Mam na mysli pewna liczbe z zakresu od 1 do 100.")
print("Spróbuj ja odgadnac w jak najmniejszej liczbie prób.")
import random
rand_num = random.randint(1, 100)
chosen = 0
counter = 0
while chosen != rand_num:
    chosen = int(input("Podaj liczbe: "))
    counter += 1
    if chosen > rand_num:
        print("Za duzo, to twoja ", counter, " proba")
    elif chosen < rand_num:
        print("Za malo, to twoja ", counter, " proba")
print("Gratulacje, szukana liczba to: ", rand_num)
print("Zgadles w ", counter, " probie")
print("\nAby zakonczyc program, naciśnij klawisz Enter")