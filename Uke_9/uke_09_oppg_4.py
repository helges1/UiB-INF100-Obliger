bok = input("Tittel: ")

in_storage = {
    "Ancillary Justice": 1_046, # vi kan bruke _ i tall, den blir ignorert
    "The Use of Weapons": 372,
    "1984": 5_332,
    "The Three-Body Problem": 523,
    "A Fisherman of the Inland Sea": 728,
}

while bok != "":
    if in_storage.get(bok) == None:
        print("Vi har", 0, "av", '"' + bok + '"')
        print()
        bok = input("Tittel: ")

    elif in_storage.get(bok) != None:
        print("Vi har", in_storage.get(bok), "av", '"' + bok + '"')
        print()
        bok = input("Tittel: ")

if bok == "":
    print("Ha det!")