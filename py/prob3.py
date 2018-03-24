#! /usr/bin/env python
# Project Euler problem 3: Find the largest prime factor of a composite number.

# Repeatedly divide by increasing divisors. Since
# we're starting with the smallest numbers, every
# new valid factor we find should be a prime
def find_prime_factors(num, start=1):
  factors = []
  largest = 0
  divisor = start
  while divisor < num:
    if num % divisor == 0:
      largest = divisor
      factors.append(divisor)
      num = int(num/divisor)
    else:
      divisor += 1
  if num >= largest:
    factors.append(num)
  return factors


if __name__ == "__main__":
  n = 600851475143
  factors = find_prime_factors(n, 2)
  max_factor = max(factors)
  print(max_factor)
