# Med hjelp fra Christoffer Slettebø
from random import randint
from collections import Counter
def kast_n_2(n):
    liste=[]
    for _ in range(n):
        liste.append(randint(1,6)+randint(1,6))
    return liste

def print_histo(xs):
    counter = Counter(range(2,13))
    for i in xs:
        counter[i]+=1
    histogram=[]
    n = len(xs)
    for i in sorted(counter.items()):
        histogram.append(f'{i[0]:2} {int((((i[1]-1)*100)/n))*"*"}')
    print("\n".join(histogram))
#print(print_histo(kast_n_2(1000)))