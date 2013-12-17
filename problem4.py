
def is_palindrome(arg1):
    word = str(arg1)
    return word == ''.join(list(reversed(word)))

max_pal = 1
for x in xrange(999, 99, -1):
    for y in xrange(999, 99, -1):
        cur = x * y
        if is_palindrome(cur):
            if max_pal < cur:
                max_pal = cur

print max_pal