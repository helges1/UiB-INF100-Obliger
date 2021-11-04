def mean(n):
    return sum(n) / len(n)

def median(n):
    sortedLst = sorted(n)
    lstLen = len(n)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def mode(n):
    most = max(list(map(n.count, n)))
    mode = list(filter(lambda x: n.count(x) == most, n))
    return mode[0]