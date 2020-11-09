# Mamy klase gdzie jest N dziewczynek i N chlopcow, ktorzy stoja w linii w jakiejs konfiguracju,
# kazdy w odstepie jednego metra od siebie. Odpowiedz na pytanie ile metrow wszyscy przejda gdy beda chcieli
# doprowadzic do postaci, ze najpierw stoja dziewczynki a potem chlopcy?
# 1 - girl, 0 - boy
# Poniewaz dziewczyny musza przejsc na miejsca chlopakow (i na odwrot), czyli ze swojego miejsca ida do srodka
# i pozniej ida tyle co chlopaki, gdy ci przchodza ze swoich miejsc na lewo
# Wniosek: dwa razy zostanie przebyta droga z lewej do srodka i dwa razy z prawej do srodka


def ile_metrow(arr):
    sr = (len(arr) - 1) // 2
    sumB = 0
    idx = 0
    while idx < sr:
        if arr[idx] == 0:
            sumB += sr - idx
        idx += 1

    sumG = 0
    while idx < len(arr):
        if arr[idx] == 1:
            sumG += idx - sr
        idx += 1

    return 2 * (sumB + sumG)

def ile_metrow2(arr):
    chlopcy = 0
    steps = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            chlopcy += 1
        else:
            steps += chlopcy * 2
    return steps
        

arr = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0]

print("Lacznie wszyscy przejda:", ile_metrow(arr), "metrow.")
print("Lacznie wszyscy przejda:", ile_metrow2(arr), "metrow. (druga wersja)")