#! /usr/bin/env python
# Project Euler problem 2: By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued
# terms.

from seqs import fibonacci
from utils import take_limit, is_even

def even_fib():
  return filter(is_even, fibonacci())

def even_fib_sum(limit):
  return sum(take_limit(even_fib(), limit))

if __name__ == "__main__":
  limit = 4000000
  print(even_fib_sum(limit))
