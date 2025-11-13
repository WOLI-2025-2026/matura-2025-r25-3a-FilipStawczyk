# Filip Stawczyk

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/symbole.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]

# [wiersz][pozycja]

liczba_kwadratów = 0
koordynaty =[]

for index_w, wiersz in enumerate(linijki[1:-1], start=1):
    for index_p, pozycja in enumerate(wiersz[1:-1], start=1):
        pozostałe = [linijki[index_w-1][index_p-1], linijki[index_w-1][index_p], linijki[index_w-1][index_p+1],
                     linijki[index_w][index_p-1], #środek 
                     linijki[index_w][index_p+1],
                     linijki[index_w+1][index_p-1], linijki[index_w+1][index_p], linijki[index_w+1][index_p+1]]
        if all(x == pozycja for x in pozostałe):
            liczba_kwadratów+= 1
            koordynaty+= [index_w+1, index_p+1]
exit = str(liczba_kwadratów) + " " + " ".join(map(str, koordynaty))
with open("wynik2_2.txt", "w") as plik:
    plik.writelines(exit)