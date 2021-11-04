import random
import collections

def kast_n_2(n):
    count = 1
    randomnumbers = []
    while count <= n:
        randomnumbers.append(random.randint(1, 6)+random.randint(1, 6))
        count += 1
    print_histo(randomnumbers)
    
def print_histo(xs):

    tall = xs
    tot = collections.Counter(tall)
    histogram = ""

    for x in range(2, 13):
        histogram += f"{x:2} {int(tot[x]/len(tall)*100)*'*'}"
        

    return(histogram)

print (kast_n_2(3444))