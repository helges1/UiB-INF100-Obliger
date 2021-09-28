def complement(dna):
    print(dna)
    print("|" * len(dna))
    # https://stackoverflow.com/questions/25188968/reverse-complement-of-dna-strand-using-python
    complement_verdi = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join([complement_verdi[verdi] for verdi in dna[::-1]])
    



