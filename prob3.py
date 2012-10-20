#! /usr/bin/env python

def largest_prime_factor (num):
  largest = 0;
  i = 2;
  while i < num:
    if (num % i) == 0:
      largest = max (largest, largest_prime_factor(num / i))
      break
    i += 1

  if largest == 0:
    return num
  else:
    return largest


print largest_prime_factor (600851475143)
