with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/dron.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]
dane = [list(map(int, linia.split())) for linia in linijki]
licznik = 0
pozycja = [0, 0]
for a in dane:
    pozycja[0]+= a[0]
    pozycja[1]+= a[1]
    if pozycja[0] > 0 and pozycja[0] < 5000 and pozycja[1] > 0 and pozycja[1] < 5000:
        licznik += 1
with open("wynik3_2_a.txt", "w") as plik:
    plik.writelines(str(licznik))