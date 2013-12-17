from __future__ import print_function


def prime_numbers_generator():
    prime_numbers = [2]
    pointer = 2
    yield pointer
    while True:
        pointer += 1
        maybe_prime = True
        upper_limit = pointer/2
        for prime in prime_numbers:
            if prime > upper_limit:
                break
            if pointer % prime:
                upper_limit = pointer/prime
            else:
                maybe_prime = False
                break
        if maybe_prime:
            prime_numbers.append(pointer)
            yield pointer

result = 0
gen = prime_numbers_generator()
while True:
    a = gen.next()
    print(a)
    if a > 2000000:
        break
    result += a

print('\n')
print(result)