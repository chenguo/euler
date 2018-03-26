#! /usr/bin/env python
# Project Euler problem 3: Find the largest prime factor of a composite number.

from utils import find_prime_factors

if __name__ == "__main__":
  n = 600851475143
  factors = find_prime_factors(n, 2)
  max_factor = max(factors)
  print(max_factor)
