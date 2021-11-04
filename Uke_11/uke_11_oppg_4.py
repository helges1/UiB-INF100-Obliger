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
    from collections import Counter
    counter = Counter(range(2,13))
    for tall in xs:
        counter[tall]+=1
    histogramet=""
    n = 3444
    for tall in sorted(counter.items()):
        histogramet+=(f'{tall[0]:2} {int((((tall[1]-1)*100)/n))*"*"}')
    print (histogramet)

print (kast_n_2(3444))