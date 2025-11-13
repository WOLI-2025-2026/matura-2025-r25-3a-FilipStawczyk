# Filip Stawczyk

def konwersja(liczba): #liczba jest w stringu
    wynik = 0
    for i in range(12):
        wynik += 3 ** (11-i) * liczba[i]
    wynik = 177147 * int(liczba[0]) + 59049 * int(liczba[1]) + 19683 * int(liczba[2]) + 6561 * int(liczba[3]) + 2187*int(liczba[4]) + 729*int(liczba[5])
    return wynik

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/symbole_przyklad.txt", "r") as plik:
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
