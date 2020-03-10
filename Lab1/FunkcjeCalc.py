def dodawanie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return "Wynik = " + str(a + b)


def odejmowanie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return "Wynik = " + str(a - b)


def mnozenie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return "Wynik = " + str(a * b)


def dzielenie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return "Wynik = " + str(a / b)


def potegowanie():
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj potege: "))
    return "Wynik = " + str((pow(a, b)))


def pierwiastkowanie():
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj stopien pierwiastka: "))
    return "Wynik = " + str(a ** (1 / b))
