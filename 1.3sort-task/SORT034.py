# Zadanie 12
# Dany jest zawierający n wierzchołków wielokąt, niekoniecznie wypukły. Jest reprezentowany jako
# tablica par struktur:
# class Point:
# x
# y
# w której (p1, p2) oznacza, że obiekty p1 i p2 klasy Point są połączone odcinkiem. Dany jest również
# punkt q, leżący poza wielokątem. Zaimplementuj/zaproponuj algorytm, który wyznaczy jak należy
# poprowadzić półprostą, zaczynającą się w punkcie q, tak aby przecięła jak najwięcej odcinków
# wielokąta. Uwaga!: zakładamy, że jeśli punkt p jest wspólny dla dwóch odcinków, to prosta
# przechodząc przez ten punkt przecina oba. Algorytm powinien działać w czasie O(nlog(n)).
# Zadanie opisowe:
# 1. Trzeba przesunac punkty takzeby q byl w (0,0)
# 2. Posortowac punkty po kacie jaki tworza z punktem (0,0)
# 3. Wybrac srodkowy i potem rekursywnie wywolac dla pierwszej polowy i drugiej'
# 4. Wybrac max z obu
