def remove_sevens(liste):
    i = [i for i in liste if i != 7]
    return i      

def every_other(liste):
    i = liste[0::2]
    return i

def reverse(liste):
    i = liste[::-1]
    return i

def double_values(liste):
    i = [i * 2 for i in liste]
    return i

def unique_values(liste):
    unikListe = []
    for word in liste:
        if word not in unikListe:
            unikListe.append(word)
    return unikListe
