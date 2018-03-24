#! /usr/bin/env python
# Project Euler problem 3: Find the largest prime factor of a composite number.

def largest_prime_factor (num, start):
  largest = 0;
  i = start
  while i < num:
    if (num % i) == 0:
      largest = max (largest, largest_prime_factor(num / i, i))
      break
    i += 1

  if largest == 0:
    return num
  else:
    return largest


print largest_prime_factor (600851475143, 2)
