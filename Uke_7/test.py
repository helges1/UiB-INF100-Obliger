# Må fikse med zip

def data_reorganize(verdi):

    return print(zip(*verdi))

    

print(data_reorganize((
  ("mandag", 16.0),
  ("tirsdag", 13.0),
  ("onsdag", 14.0),
  ("torsdag", 13.0),
  ("fredag", 15.0),
  ("lørdag", 13.0),
)))