

def gnrtr():
    x = 2
    while True:
        s = str(x)
        sum_of_digits = 0
        for digit in s:
            sum_of_digits += int(digit)
        x *= 2
        yield sum_of_digits

a = gnrtr()
for i in xrange(1000):
    b = a.next()

print i, b


