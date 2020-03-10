n = int(input("Podaj ile liczb chcesz wprowadzić: "))
wynik = 0;
for i in range(1, n + 1):
    wynik = wynik + float(input("Podaj " + str(i) + " liczbe: "))
print("Wynik wynosi", wynik)

# print(float(input("podaj liczbe")) + float(input("podaj liczbe")))
