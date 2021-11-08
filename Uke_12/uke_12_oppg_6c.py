import csv

lats = []
lons = []
lats_salt = []
lons_salt = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        if row[20] == 'FERSKVANN':

            try:
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            except ValueError:
                continue
            lats.append(lat)
            lons.append(lon)
        if row[20] == 'SALTVANN':

            try:
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            except ValueError:
                continue
            lats_salt.append(lat)
            lons_salt.append(lon)

try:
    import matplotlib.pyplot as plt
    # Blå prikker er saltvann, røde prikker er ferskvann (Kan byttes ut med "+" for å bytte tegn.)
    plt.plot(lons_salt,lats_salt,'.b')
    plt.plot(lons,lats,'.r')
    plt.savefig("uke_12_oppg_6c.png")
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
    print(f'We have {len(lats_salt)} latitudes and {len(lons_salt)} longitudes')