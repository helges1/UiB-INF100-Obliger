navn = input("Hva er ditt navn? ")
adresse = input("Hva er din adresse? ")
post = input("Hva er ditt postnummer og poststed? ")

navn_len = len(navn)
adresse_len = len(adresse)
post_len = len(post)

maks = max(navn_len, adresse_len, post_len) 

print()

if navn_len == maks:
    print(navn)
if adresse_len == maks:
    print(adresse)
if post_len == maks:
    print(post)
