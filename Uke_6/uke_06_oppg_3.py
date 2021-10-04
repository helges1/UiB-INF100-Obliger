def complement(dna):
    print(dna)
    print("|" * len(dna))
    comp_verdi = []
    for i in dna:
        if i == "T":
            comp_verdi.append("A")
        if i == "A":
            comp_verdi.append("T")
        if i == "G":
            comp_verdi.append("C")
        if i == "C":
            comp_verdi.append("G")

    return ''.join(reversed(comp_verdi))





