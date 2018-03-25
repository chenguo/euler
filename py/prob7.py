#! /usr/bin/env python
# Project Euler problem 6:
# what is the 10,001st prime number?

from itertools import islice
from prob1 import contains_factor

def gen_primes():
    primes = []
    i = 2
    while True:
        if not contains_factor(i, primes):
            yield i
            primes.append(i)
        i += 1

if __name__ == "__main__":
    n = 100
    top_n_primes = list(islice(gen_primes(), n))
    print(top_n_primes[n-1])
