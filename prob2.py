#! /usr/bin/env python
# Project Euler problem 2: By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued
# terms.

from itertools import takewhile

def fibonacci():
  a = 0
  b = 1
  while(True):
    fib = a + b
    yield fib
    a = b
    b = fib

def is_even(x):
  return x % 2 == 0

def even_fib():
  return filter(is_even, fibonacci())

def even_fib_sum(limit):
  limited_even_fibs = takewhile(lambda x: x < limit, even_fib())
  return sum(limited_even_fibs)


if __name__ == "__main__":
  limit = 4000000
  print(even_fib_sum(limit))
