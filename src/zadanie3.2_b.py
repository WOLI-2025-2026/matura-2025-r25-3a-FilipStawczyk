with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/dron_przyklad.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]
dane = [list(map(int, linia.split())) for linia in linijki]
