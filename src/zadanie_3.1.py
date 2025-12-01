def nwd(a, b):
    dzielnik = max(a, b)
    while dzielnik > 1:
        if a%dzielnik==0 and b%dzielnik==0:
            return dzielnik
        else:
            dzielnik-=1
    return 1

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/dron.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]
dane = [list(map(int, linia.split())) for linia in linijki]
for a in range(len(dane)):
    for b in range(len(dane[a])):
        if dane[a][b] < 0:
            dane[a][b]*= -1

licznik = 0
for a in range(len(dane)): #dane[a] to [pierwsza, druga]
    if nwd(dane[a][0], dane[a][1]) > 1:
        licznik += 1

with open("wynik3_1.txt", "w") as plik:
    plik.writelines(str(licznik))