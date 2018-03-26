#! /usr/bin/env python
# Project Euler problem 7:
# what is the 10,001st prime number?

from itertools import islice
from seqs import gen_primes

if __name__ == "__main__":
    n = 10001
    top_n_primes = list(islice(gen_primes(), n))
    print(top_n_primes[n-1])
