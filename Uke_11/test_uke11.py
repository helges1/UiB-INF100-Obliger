import collections
from decimal import *
class NoPrice(Exception):
    pass
class NotEnoughPaid(Exception):
    pass

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    # Skiller kjøp/salg fra produkt
    input_file = open(cash_register_filename, 'r') 
    produkt = []
    status = []

    for line in input_file:
        sales, cost = map(str, line.split(";"))
        status.append (sales)
        produkt.append (cost.strip("\n"))

    produkt_status = list(zip(produkt, status))
    produkt_buy = []
    produkt_return = []

    for i in range(len(produkt_status)):
        if produkt_status[i][1] == "buy":
            produkt_buy.append(produkt_status[i][0])
        if produkt_status[i][1] == "return":
            produkt_return.append(produkt_status[i][0])
   
    # Finne ut hvor mye som kjøpes av hvert produkt

    antall_buy = collections.Counter(produkt_buy)
    antall_return = collections.Counter(produkt_return)
    
    # Fikser rekkefølge

    sort_buy = sorted(antall_buy)
    sort_return = sorted(antall_return)
    
    # Brukes til å legge til tall senere
    sort_antall_buy = []
    for i in sort_buy:
        sort_antall_buy.append(int(antall_buy[i]))

    sort_antall_return = []
    for i in sort_return:
        sort_antall_return.append(int(antall_return[i]/-1))
   
    # Skiller proodukt fra pris
    input_file = open(prices_filename, 'r') 
    prod = []
    pris = []

    for line in input_file:
        product, cost = map(str, line.split(";"))
        prod.append (product)
        pris.append (cost.strip("\n"))

    produkt_pris = list(zip(prod, pris))
    produkt_pris = sorted(produkt_pris)


    # Hente ut priser
    pris_buy = []
    pris_return = []

    for i, p in produkt_pris:
        if i in sort_buy:
            pris_buy.append(p)
        if i in sort_return:
            pris_return.append(p)

    # Regner ut totalen
    total_pris_buy = []
    total_pris_return = []

    i = 0
    while i < len(pris_buy):
        total_pris_buy.append(Decimal(pris_buy[i])*Decimal(sort_antall_buy[i]))
        i+=1
    j = 0
    while j < len(pris_return):
        total_pris_return.append(Decimal(pris_return[j])*Decimal(sort_antall_return[j]))
        j+=1
    
    purcases_returns = list(zip(sort_antall_buy, sort_buy, total_pris_buy))

    alt_return = list(zip(sort_antall_return, sort_return, total_pris_return))

    for i in range(len(alt_return)):
        purcases_returns.append(alt_return[i])

    # Dette er alle varene i rekkefølge
    purcases_returns = list(purcases_returns)

    # Finne total
    priser=[]
    for antall, produkt, pris in purcases_returns:
        priser.append(pris)
    
    total = Decimal(sum(priser))

    # Finne MVA - (VAT)

    vat = Decimal(total) * Decimal(0.2)
    

    # Finne betaling
    pay=[]
    for i in range(len(produkt_status)):
        
        if produkt_status[i][1] == "pay":
            pay.append(Decimal(produkt_status[i][0]))

    
    payment = sum(pay)


    # veksel
    change = total - payment

    if payment <= total:
        raise NotEnoughPaid
    else:
        return purcases_returns, total, vat, payment, change

def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)

print(receipt("prices.txt", "cash_register.txt"))