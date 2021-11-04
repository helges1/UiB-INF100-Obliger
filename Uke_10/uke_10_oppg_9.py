def rename_all(namelist):
    for i in namelist:
        rename_from_data(i)

def rename_from_data(filename):
    with open(filename, encoding="utf8") as f:
        liste_fil = []
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            liste_fil.append(line_list)

        sted = ''.join(liste_fil[0])
        dato = ''.join(liste_fil[1])

        nytt_filnavn = (f"{dato}_{sted}.txt")

        liste_fil.remove(liste_fil[0])
        liste_fil.remove(liste_fil[0])

    with open(nytt_filnavn, "w", encoding="utf8") as f:
        for i in range(len(liste_fil)):
            f.write(f"{liste_fil[i][0]} {liste_fil[i][1]} {liste_fil[i][2]} {liste_fil[i][3]}\n")

print(rename_from_data("qwerty.txt"))

# namelist = ["qwghlm.txt", "qwerty.txt"]
# print(rename_all(namelist))