# Modifisert utgave for å unngå å bruke rjust, men eller kun benytte metoder som er blitt lært bort i forelesningen

a = input("Første raden: ")
b = input("Andre raden: ")
c = input("Tredje raden: ")

d = len(a)
e = len(b)
f = len(c)

maks = max(d, e, f)
ramme = "@" * maks + "@@@@"

print()
print(ramme)
print("@" + " " * (maks - d), a, "@")
print("@" + " " * (maks - e), b, "@")
print("@" + " " * (maks - f), c, "@")
print(ramme)          