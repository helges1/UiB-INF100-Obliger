def draw_haiku_frame(first, second, third):
    first_len = len(first)
    second_len = len(second)
    third_len = len(third)

    maks = max(first_len, second_len, third_len)
    
    maksAlfa = "@" * maks
    maks1 = " " * (maks - first_len)
    maks2 = " " * (maks - second_len)
    maks3 = " " * (maks - third_len)

    ramme = f"@{maksAlfa}@@@" 
    linje1 = f"@ {maks1}{first} @" 
    linje2 = f"@ {maks2}{second} @" 
    linje3 = f"@ {maks3}{third} @"  

    return ramme + "\n" + linje1 + "\n" + linje2 + "\n" + linje3 + "\n" + ramme