__author__ = 'a.khadiev'

square_of_sum_of_100 = (100 * 101 / 2) ** 2

sum_of_square_of_100 = 0
for x in xrange(1, 101):
    sum_of_square_of_100 += x**2

print sum_of_square_of_100-square_of_sum_of_100