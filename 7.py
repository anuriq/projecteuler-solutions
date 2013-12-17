from __future__ import print_function


def prime_numbers_generator():
    prime_numbers = [2]
    pointer = 2
    yield pointer
    while True:
        maybe_prime = True
        for prime in prime_numbers:
            if not pointer % prime:
                maybe_prime = False
                break
        if maybe_prime:
            prime_numbers.append(pointer)
            yield pointer
        else:
            pointer += 1

gen = prime_numbers_generator()
for x in xrange(10001):
    print('.', end='')
    a = gen.next()

print('\n')
print(a)