#Filip Stawczyk

with open("/workspaces/matura-2025-r25-3a-FilipStawczyk/zalaczniki-2025/symbole.txt", "r") as plik:
    linijki = [linia.strip() for linia in plik.readlines()]

palindromy = []

for linia in linijki:
    if linia == linia[::-1]:
        palindromy.append(linia)

for p in palindromy:
    print(p)
