from Lab1.FunkcjeCalc import *

x = int(
    input("Wybierz operacje:\n1.Dodawanie\n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n5.Potegowanie\n6.Pierwiastkowanie "))
if x == 1:
    print(dodawanie())
elif x == 2:
    print(odejmowanie())
elif x == 3:
    print(mnozenie())
elif x == 4:
    print(dzielenie())
elif x == 5:
    print(potegowanie())
elif x == 6:
    print(pierwiastkowanie())
