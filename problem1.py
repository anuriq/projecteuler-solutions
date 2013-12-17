
from __future__ import print_function
import time


def is_multiple_of_number(number, target):
    if target % number:
        return False
    else:
        return True


mysum = 0
start = time.time()
for x in xrange(1000000):
    if is_multiple_of_number(3, x):
        mysum += x
    elif is_multiple_of_number(5, x):
        mysum += x

print('Execution time:', (time.time() - start) * 1000, 'ms')
print(mysum)