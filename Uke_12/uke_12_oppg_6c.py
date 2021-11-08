import csv

lats_fersk = []
lons_fersk = []

lats_salt = []
lons_salt = []



with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        if row[20]=="FERSKVANN":

            try:
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            except ValueError:
                continue
            lats_fersk.append(lat)
            lons_fersk.append(lon)

            
    for row in akvareader:
        if row[20]=="SALTVANN":

            try:
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            except ValueError:
                continue
            lats_fersk.append(lat)
            lons_fersk.append(lon)
  
    

try:
    import matplotlib.pyplot as plt
    plt.plot(lons_fersk,lats_fersk,'+b')
    plt.plot(lons_salt,lats_salt,'+r')
    plt.savefig("uke_12_oppg_6c.png")
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats_fersk)} latitudes and {len(lons_fersk)} longitudes')
    print(f'We have {len(lats_salt)} latitudes and {len(lons_salt)} longitudes')

