from itertools import combinations

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/dron.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]
dane = [list(map(int, linia.split())) for linia in linijki]

pozycja = [0, 0]
punkty = []
for i in dane:
    pozycja[0]+= i[0]
    pozycja[1]+= i[1]
    punkt = [0, 0]
    punkt[0]=pozycja[0]
    punkt[1]=pozycja[1]
    punkty.append(punkt)

for a, b in combinations(punkty, 2):
    sprawdzany_p = [0, 0]
    sprawdzany_p[0] = (max(a[0], b[0]) - min(a[0],b[0]))/2
    sprawdzany_p[1] = (max(a[1], b[1]) - min(a[1],b[1]))/2
    sprawdzany = [min(a[0], b[0])+sprawdzany_p[0], min(a[1], b[1])+sprawdzany_p[1]]
    if sprawdzany in punkty:
        wynik = f"({min(a[0], b[0])}, {min(a[1], b[1])}), ({int(sprawdzany[0])}, {int(sprawdzany[1])}), ({max(a[0], b[0])}, {max(a[1], b[1])})"
        with open("wynik3_2_b", "w") as plik:
            plik.writelines(wynik)