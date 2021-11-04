# import itertools

# def card_combinations(k, n):
#     bases = [2,3,4,5,6,7,8,9,10,11]

#     liste = []
    
#     for i in itertools.product(bases, repeat=k):
#         if sum(i) == n:
            
#             liste.append((i)) 

#     return liste


# print(card_combinations(1, 10))


import itertools 

cards=[2,3,4,5,6,7,8,9,10,11]

new_list=[]

def card_combinations(k,n):

    for x in itertools.combinations (cards,k):

        if sum(x)==n:

            new_list.append(x)

    return new_list

print(card_combinations(2, 10))