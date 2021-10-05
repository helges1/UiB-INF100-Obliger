def data_reorganize(verdi):

    dager = []
    temperatur = []
    for dag in verdi:
        dager.append(dag[0])
            
    for temp in verdi:
        temperatur.append(temp[1])

    dager = tuple(dager)
    temperatur = tuple(temperatur)

    alt = dager, temperatur

    return alt

# print(data_reorganize((
#   ("mandag", 16.0),
#   ("tirsdag", 13.0),
#   ("onsdag", 14.0),
#   ("torsdag", 13.0),
#   ("fredag", 15.0),
#   ("lørdag", 13.0),
# )))

# Kan også løses med zip
#
#