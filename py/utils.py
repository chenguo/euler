from itertools import takewhile

def take_limit(seq, limit):
    return takewhile(lambda n: n < limit, seq)

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
