def hvem_eldst(navn1, alder1, navn2, alder2):
    navn1 = str(navn1)
    alder1 = int(alder1)
    navn2 = str(navn2)
    alder2 = int(alder2)

    maks = max(alder1, alder2)

    if alder1 >= maks:
        eldst = f"{navn1} er {alder1} år og eldst."
    
    if alder2 >= maks:
        eldst = f"{navn2} er {alder2} år og eldst."

    return eldst