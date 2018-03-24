#! /usr/bin/env python
# Project Euler problem 3: Find the largest prime factor of a composite number.

# Repeatedly divide by increasing divisors. Since
# we're starting with the smallest numbers, every
# new valid factor we find should be a prime
def largest_prime_factor(num, start=2):
  largest = 0;
  factor = start
  while factor < num:
    if (num % factor) == 0:
      largest = factor
      num = int(num/factor)
    else:
      factor += 1
  return max(largest, num)


if __name__ == "__main__":
  n = 600851475143
  print(largest_prime_factor(n))
