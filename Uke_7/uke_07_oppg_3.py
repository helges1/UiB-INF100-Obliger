def adjust_daily_temps(verdier):
    alle_temp = list(verdier)
    tors = list(alle_temp[3])
    tors[1] = 12.0
    alle_temp[3] = tuple(tors)
    return tuple(alle_temp)

# print(adjust_daily_temps((
#   ("mandag", 16.0),
#   ("tirsdag", 13.0),
#   ("onsdag", 14.0),
#   ("torsdag", 13.0),
#   ("fredag", 15.0),
#   ("lørdag", 13.0),
# )))