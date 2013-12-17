from __future__ import print_function

start = (0, 0)


def fun(n):
    if n == 1:
        return 2
    return 4*fun(n-1) - 4*n + 6

print(fun(2))
print(fun(3))
print(fun(20))