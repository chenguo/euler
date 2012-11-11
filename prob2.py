#! /usr/bin/env python
# Project Euler problem 2: By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued
# terms.

def fib_sum (limit):
  total = 0
  val = 2
  prev = 1
  while val < limit:
    if (val & 1) == 0:
      total += val
    tmp = val
    val += prev
    prev = tmp
  return total

print fib_sum(4000000)
