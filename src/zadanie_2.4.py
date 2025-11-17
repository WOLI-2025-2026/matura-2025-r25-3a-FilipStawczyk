# Filip Stawczyk

def konwersja(liczba): #liczba jest w stringu
    wynik = 0
    for i in range(12):
        wynik += 3 ** (11-i) * int(liczba[i])
    return wynik

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/symbole.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]

suma = 0

for linia in linijki:
    wynik = ""
    for znak in linia:
        if znak == "o":
            wynik += "0"
        elif znak == "+":
            wynik += "1"
        elif znak == "*":
            wynik += "2"
    suma += konwersja(wynik)

a = str(suma)
znaczkowe = ""
while suma >0:
    if suma % 3 == 0:
        znaczkowe += "o"
    elif suma % 3 == 1:
        znaczkowe += "+"
    elif suma % 3 == 2:
        znaczkowe += "*"
    suma = suma // 3
exit_z = znaczkowe[::-1]
with open("wynik2_4.txt", "w") as plik:
    plik.writelines(a + " " + exit_z)