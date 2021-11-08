def mean(n):
    return sum(n) / len(n)

def median(n):
    sortedList = sorted(n)
    listLen = len(n)
    index = (listLen - 1) // 2
   
    if (listLen % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0

def mode(n):
    most = max(list(map(n.count, n)))
    mode = list(filter(lambda x: n.count(x) == most, n))
    return mode[0]