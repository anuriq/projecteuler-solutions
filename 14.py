
def gen(n):
    yield n
    while True:
        if n == 1:
            raise StopIteration
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1
        yield n




m = 1
for i in xrange(2, 1000000):
    l = len(list(gen(i)))
    print i, l
    if l > m:
        m = l
        result = i

print result