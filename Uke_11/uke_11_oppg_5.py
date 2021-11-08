from decimal import Decimal
class NoPrice(Exception):
    pass
class NotEnoughPaid(Exception):
    pass

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    #Leser prices filen og legger varene til i en dictionary
    Product_price = {}
    with open (prices_filename, "r") as f:
        for line in f:
            product, price = line.split(';')
            Product_price.update({product: Decimal(price)})

    #Leser cash_register filen og sorterer varene på om de blir kjøpt, returnert eller betalt for inn i forskjellige dictionaries 
    buy = {}
    retur = {}
    paid = 0
    with open(cash_register_filename, "r") as fil:
        for line in fil:
            actin, product = line.strip().split(";")
            if actin == "buy":
                if product in buy:
                    buy[product] = buy[product] + 1
                else:
                    buy[product] = 1
            elif actin == "return":
                if product in retur:
                    retur[product] = retur[product] + 1
                else:
                    retur[product] = 1
            elif actin == "pay":
                paid += Decimal(product)

    totalprice = 0
    purcases_returns = []
    #Finner den totale prisen for alle varene, og lager listen som skal returneres med total, produkt og totalpris
    for product, total in sorted(buy.items()):
        if product not in Product_price:
            raise NoPrice
        totalprice_product = total * Product_price[product]
        totalprice += totalprice_product
        purcases_returns.append((total, product, totalprice_product))
    for product, total in sorted(retur.items()):
        if product not in Product_price:
            raise NoPrice
        totalprice_product = total * Product_price[product]
        totalprice -= totalprice_product
        purcases_returns.append((-total, product, -totalprice_product))
    
    #regner ut mva
    vat = totalprice * Decimal("0.2")

    #sjekker om kunden har betalt hele beløpet
    if paid < totalprice:
        raise NotEnoughPaid
    
    #regner ut hvor mye som har blitt change (negativt tall)
    change = totalprice - paid

    return (purcases_returns, totalprice, vat, paid, change)


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

#print(receipt("prices.txt", "cash_register.txt"))

