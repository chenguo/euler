#! /usr/bin/env python
# Project Euler problem 10:
# Sum primes below 10,000,000

from seqs import gen_primes, gen_primes_v2
from utils import take_limit

if __name__ == "__main__":
    limit = 2e6
    total = sum(take_limit(gen_primes(), limit))
    print(total)
