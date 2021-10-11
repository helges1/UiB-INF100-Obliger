def return_change(payment, price):

    coins = [1, 5, 10, 20]

    pris = price
    betalt = payment

    diff = betalt - pris
    veksel = []

    for c in coins[::-1]:

        while diff >= c:
            diff -= c
            veksel.append(c)

    return veksel

# print(return_change(30, 13))