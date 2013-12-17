
for a in xrange(1000):
    for b in xrange(a+1, 1000):
        c = 1000 - b - a
        if (a**2 + b**2) == c**2:
            print a,b,c

