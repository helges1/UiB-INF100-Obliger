a = int(input("Factor A: "))
b = int(input("Factor B: "))

størst = max(a,b)
minst = min(a,b)

print("=========================")

count = 0
max_count = 0
max_count1 = 0
tall_a = 1
a_tall = []

while tall_a <= minst :
    a_tall.append(tall_a)

    if tall_a == 1:
        tall_a += 1 
        count += 1

    else:
        tall_a = tall_a *2
        count += 1
    
b_tall = []
while count > 0:
    b_tall.append(størst)
    størst = størst * 2
    count -= 1
    max_count += 1
    max_count1 += 1

def print_x(minst):
    mins = a_tall
    x = []

    for c in mins[::-1]:
        
        while minst >= c:
            x.append("X")
            minst -= c
            break

        else:
            x.append(" ")   
            
    return x[::-1]

X = print_x(minst)

while max_count > 0:
    print(f"{X[count]} {a_tall[count]: >4} {b_tall[count]: >4}")
    max_count -= 1
    count += 1

print("=========================")

plasser_med_x = [i for i, e in enumerate(X) if e == "X"]

len_x = len(plasser_med_x)

teller = 0
a_tall_liste =[]

while teller < len_x:
    a_tall_liste.append(a_tall[plasser_med_x[teller]])
    teller += 1

teller = 0
b_tall_liste =[]

while teller < len_x:
    b_tall_liste.append(b_tall[plasser_med_x[teller]])
    teller += 1

a_list_str = list(map(str,a_tall_liste))
print (' + '.join(a_list_str), "=", sum(a_tall_liste))

b_list_str = list(map(str,b_tall_liste))
print (' + '.join(b_list_str), "=", sum(b_tall_liste))

print("=========================")

print(f"{a} * {b} = {a * b}")