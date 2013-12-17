from __future__ import print_function


def generate_fibonacci():
    last_pair = [1, 2]
    yield last_pair[0]
    yield last_pair[1]
    while True:
        current_number = sum(last_pair)
        yield current_number
        last_pair.pop(0)
        last_pair.append(current_number)

my_sum = 0
for x in generate_fibonacci():
    if x > 4000000:
        break
    if not x % 2:
        my_sum += x

print(my_sum)