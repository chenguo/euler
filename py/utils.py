from itertools import takewhile

def take_limit(seq, limit):
    return takewhile(lambda n: n < limit, seq)
