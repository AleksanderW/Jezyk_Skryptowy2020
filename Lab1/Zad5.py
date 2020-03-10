from datetime import date

date = date(int(input("Podaj rok: ")), int(input("Podaj miesiac:")), int(input("Podaj dzien: ")))
print(date.today() - date)
