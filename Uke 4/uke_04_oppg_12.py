binær_tall = input('Binært tall: ')
maks_lengde = len(binær_tall)
total = 0

for i in binær_tall:
    titallsystem = total + int(i) * 2 ** (maks_lengde - 1)
    total = titallsystem
    maks_lengde -= 1

print(titallsystem)