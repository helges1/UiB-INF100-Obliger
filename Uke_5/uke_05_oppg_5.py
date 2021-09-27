def egen_abs(a):
    if a >= 0:
        a = a
    if a < 0: 
        a = a - a*2
    return a

def egen_max(a,b):
    maks = int((a+b+abs(a-b))/2)
    return maks

def egen_min(a,b):
    mini = int((a+b-abs(a-b))/2)
    return mini

def egen_len(a):

    lengde = 0

    for i in (a):
        lengde += 1

    return lengde