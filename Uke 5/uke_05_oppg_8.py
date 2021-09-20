def stones_to_pounds(Vstones):
    pounds = Vstones * 14
    return pounds

def stones_to_kg(Vstones):
    kg = Vstones / 0.15747
    return kg

def pounds_to_kg(V):
    kg = V / 2.20462
    return kg

def imperial_to_metric(Vstones, Vpounds):
    pounds = Vstones * 14
    pounds = pounds + Vpounds
    kg = round(pounds / 2.20462, 2)
    return kg