def tuple_repack(verdi1, verdi2):
    list1 = list(verdi1)
    list2 = list(verdi2)
    personlighet = (list1[1],list2[1])
    nyList = list(personlighet)
    return nyList

# Så at det ble tipset om å bruke Zip. Så dette etter jeg gikk videre til oppgave b 😂

# print(tuple_repack(("Princess Sparkle", "aloof", "tuna"), ("Mr Cat", "energetic", "cream")))