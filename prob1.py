#! /usr/bin/env python
# Project Euler problem 1: Add all the natural numbers below one thousand that
# are multiples of 3 or 5.

# Find sum of all multiples of N in MAX
def mult_sum (n, max):
  n_mults = (max-1) / n
  multiplier = n_mults * (1 + n_mults) / 2
  sum = n * multiplier
  return sum

sum3 = mult_sum(3, 1000)
sum5 = mult_sum(5, 1000)
sum15 = mult_sum(15, 1000)
print sum3 + sum5 - sum15
