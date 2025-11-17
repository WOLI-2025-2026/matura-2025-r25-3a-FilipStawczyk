# Filip Stawczyk

def konwersja(liczba): #liczba jest w stringu
    wynik = 0
    for i in range(12):
        wynik += 3 ** (11-i) * int(liczba[i])
    return wynik

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/symbole.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]

dziennik = {}

for linia in linijki:
    wynik = ""
    for znak in linia:
        if znak == "o":
            wynik += "0"
        elif znak == "+":
            wynik += "1"
        elif znak == "*":
            wynik += "2"
    dziennik[linia]=wynik

najwiekszy_klucz = max(dziennik, key=dziennik.get)
with open("wynik2_3.txt", "w") as plik:
    plik.writelines(str((konwersja(dziennik[najwiekszy_klucz]))) + " " + najwiekszy_klucz + "\n")