def median(l):
    l.sort()
    if len(l)==1:
        return l[0]
    if len(l) % 2 != 0:
        return l[len(l)/2]
    else:
        return (l[len(l)/2] + l[len(l)/2 - 1]) / 2.0

print median([4,5,5,4])