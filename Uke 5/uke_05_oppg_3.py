def name_age(navn, alder):
    navn = str(navn)
    alder = int(alder)
    print(navn, "er", alder, "år gammel.")
    return name_age

print(name_age("Ola", 7))