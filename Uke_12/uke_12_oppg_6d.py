# Lag et kakediagram over de ulike formolene som er oppgitt i .csv filen.

import csv
import matplotlib.pyplot as plt

akvadict = {}

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')

    for row in akvareader:
        if row[10] in akvadict:
            akvadict[row[10]] += 1
        else:
            akvadict[row[10]] = 1

    akvalist = (sorted(akvadict.items(), key=lambda x: x[0]))

    akvalist.pop(0)
    akvalist.pop(0)

    formål = []
    antall = []
    
    for i in akvalist:
        formål.append(i[0])
        antall.append(i[1])



    title = plt.title('Kakediagram over formål😋')
    title.set_ha("left")
    plt.gca().axis("equal")
    pie = plt.pie(antall, startangle=0)
    labels=formål
    plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
            bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)



    plt.savefig("uke_12_oppg_6d.png")

    plt.show()







