#! /usr/bin/env python

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
