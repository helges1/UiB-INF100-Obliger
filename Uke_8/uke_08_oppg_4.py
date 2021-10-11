a = int(input("Faktor A: "))
b = int(input("Faktor B: "))

størst = max(a,b)
minst = min(a,b)

print("=========================")

count = 0
max_count = 0
max_count1 = 0
tall_a = 1
a_tall = []

while tall_a < minst :
    a_tall.append(tall_a)

    if tall_a == 1:
        tall_a += 1 
        count += 1

    else:
        tall_a = tall_a * 2
        count += 1
    
b_tall = []
while count > 0:
    b_tall.append(størst)
    størst = størst * 2
    count -= 1
    max_count += 1
    max_count1 += 1


def print_x(minst):
    coins = a_tall
    x = []

    for c in coins[::-1]:
        
        while minst >= c:
            
            x.append("X")
            minst -= c
            break
        else:
            
            x.append(" ")   
            
    return x[::-1]

X = print_x(minst)

while max_count > 0:
    print(f"{X[count]}    {a_tall[count]}     {b_tall[count]}")
    max_count -= 1
    count += 1

print("=========================")




