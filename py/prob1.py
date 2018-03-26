#! /usr/bin/env python
# Project Euler problem 1: Add all the natural numbers below one thousand that
# are multiples of 3 or 5.

from utils import take_limit, contains_factor
from seqs import inf_range

def gen_multiples(factors):
  for n in inf_range():
    if contains_factor(n, factors):
      yield n

def fizz_buzz_sum(factors, limit):
  nums = gen_multiples(factors)
  return sum(take_limit(nums, limit))

if __name__ == "__main__":
  limit = 1000
  factors = [3, 5]
  result = fizz_buzz_sum(factors, limit)
  print(result)
