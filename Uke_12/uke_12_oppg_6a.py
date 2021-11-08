import csv

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    akvadict = {}
    for row in akvareader:
        if row[12] in akvadict:
            akvadict[row[12]] += 1
        else:
            akvadict[row[12]] = 1


    akvalist = (sorted(akvadict.items(), key=lambda x: x[0]))

    akvalist.pop(0)
    akvalist.pop(0)

    for i in akvalist:
        print(f"{i[0]}: {i[1]}")



  




