from itertools import combinations

cards=[2,3,4,5,6,7,8,9,10,11]

def card_combinations(k,n):
    new_list=[]
    combo = combinations (cards, k)
    for i in combo:
        if sum(i)==n:
            new_list.append(i)
    return new_list

#print(card_combinations(2, 10))