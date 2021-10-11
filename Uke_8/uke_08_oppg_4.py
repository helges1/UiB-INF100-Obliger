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

# Sette Xer

# a_tall_rev = a_tall[::-1]
# X = []
# tot = 0
# telle = 0
# while max_count1 > 0 :

#     if tot <= minst and 16 < tot +  a_tall_rev[telle] :

#         X.append("X")
#         max_count1 -= 1
#         tot += a_tall_rev[telle]
#         telle += 1
        
        
#     else:
#         X.append(" ")
#         max_count1 -= 1

#         telle += 1
#     print(tot)

# X = X[::-1]

se på oppgave 1

while max_count > 0:
    print(f"    {a_tall[count]}     {b_tall[count]}")
    max_count -= 1
    count += 1




