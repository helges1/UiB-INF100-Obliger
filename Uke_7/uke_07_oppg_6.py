def pigify(verdi):
    vokal = ('a','e','i','o','u','æ','ø','å','A','E','I','O','U','Æ','Ø','Å')
    ord = [char for char in verdi] 
    if ord[0] in vokal:
        translate = f"{verdi}way"
    else:
        pass
        
    return translate

print(pigify("apple"))