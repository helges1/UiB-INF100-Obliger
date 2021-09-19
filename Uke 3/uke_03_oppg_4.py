aar = int(input("Angi år: "))

if aar % 400 == 0:
    print("Dette er et skuddår.")
elif aar % 100 == 0:
    print("Dette er ikke et skuddår.") 
elif aar % 4 == 0:
    print("Dette er et skuddår.")
else:
    print("Dette er ikke et skuddår.")
