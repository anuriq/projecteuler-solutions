

def triangular_number_generator():
    n = 10000
    while True:
        number = n * (n + 1) / 2
        yield number
        n += 1


def count_divisors(n):
    count = 0
    x = 1
    while x < n/x:
        if n % x == 0:
            count += 2
        x += 1
    return count

for t in triangular_number_generator():
    c = count_divisors(t)
    print c, t
    if c > 500:
        break
