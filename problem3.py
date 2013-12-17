from __future__ import print_function

my_number = 600851475143


def factor(number):
    i = 2
    while True:
        if i > number/2:
            break
        if not number % i:
            return i
        i += 1
    return 1

x = factor(my_number)
while x != 1:
    my_number /= x
    x = factor(my_number)


print(my_number)