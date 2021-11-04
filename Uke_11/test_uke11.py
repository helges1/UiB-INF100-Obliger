import collections

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    # finne produkter som kjøpes
    cash_reg_file = open(cash_register_filename)
    lines = cash_reg_file.read()
    cash_reg_lists = lines.splitlines()
    list_buy = []

    count = 0
    while count < len(cash_reg_lists):
        if cash_reg_lists[count][0:3] == "buy":
            list_buy.append(cash_reg_lists[count][4:])
            count += 1
        else:
            pass
            count += 1
    
    # finner antall av produkter
    antall = collections.Counter(list_buy)

    

    
    


    input_file = open(prices_filename, 'r') 

    produkt = []
    pris = []
    supply = []
    for line in input_file:
        sales, cost = map(str, line.split(";"))
        produkt.append (sales)
        pris.append (cost.strip("\n"))

     
        
        count = 0
        while count < len(produkt):
            supply.append(antall[produkt[count]])
            count += 1
   

    
    samlet = zip(supply, produkt, pris)  
    


    print(len(produkt))
    print(antall)
    print("-----")
    print(list(samlet))


    


    
print(receipt_content("prices.txt", "cash_register.txt"))

